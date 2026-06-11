import requests
from json import JSONDecodeError
from pyflowlauncher import Plugin, Result, Method, api as API
from pyflowlauncher.icons import WARNING,ERROR

class Query(Method):
    def __init__(self, plugin):
        super().__init__()
        self.plugin = plugin

    def __call__(self, query: str):
        
        siyuan_api_url = self.plugin.settings.get("siyuan_api_url")
        siyuan_api_token = self.plugin.settings.get("siyuan_api_token")

        if not siyuan_api_token:
            self.add_result(Result(
                title="SiYuan API Token Missing",
                subtitle="Please configure your SiYuan API Token in plugin settings.",
                icon=WARNING
            ))
            return self.return_results()

        if not siyuan_api_url:
            self.add_result(Result(
                title="SiYuan API URL Missing",
                subtitle="Please configure your SiYuan API URL in plugin settings.",
                icon=WARNING
            ))
            return self.return_results()

        try:
            headers = {
                "Authorization": f"Token {siyuan_api_token}",
                "Content-Type": "application/json"
            }
            payload = {
                "stmt": f"SELECT id, content FROM blocks WHERE content LIKE '%{query}%' LIMIT 20"
            }
            response = requests.post(
                f"{siyuan_api_url}/api/query/sql",
                headers=headers,
                json=payload
            )
            response.raise_for_status()

            try:
                search_results = response.json()
            except JSONDecodeError:
                self.add_result(Result(
                    title="SiYuan API Response Error",
                    subtitle=f"SiYuan API returned non-JSON response. Raw content: {response.text[:200]}",
                    icon=ERROR
                ))
                return self.return_results()

            if search_results and search_results.get("code") == 0 and search_results.get("data"):
                for item in search_results["data"]:
                    block_id = item.get("id")
                    content = item.get("content", "No content available")

                    title = content.split('\n')[0] if content else "Untitled Block"
                    if len(title) > 50:
                        title = title[:50] + "..."

                    siyuan_url = f"siyuan://blocks/{block_id}"

                    result_item = Result(
                        title=title,
                        subtitle=f"Block ID: {block_id} - {content}",
                        icon="Images/siyuan.png",
                        json_rpc_action=API.shell_run(f"start {siyuan_url}")
                    )
  
                    self.add_result(result_item)
            else:
                self.add_result(Result(
                    title="No results found",
                    subtitle=f"No SiYuan notes found for '{query}'",
                    icon="Images/siyuan.png"
                ))

        except requests.exceptions.ConnectionError:
            self.add_result(Result(
                title="Connection Error",
                subtitle=f"Could not connect to SiYuan at {siyuan_api_url}. Is SiYuan running and API enabled?",
                icon=ERROR
            ))
        except requests.exceptions.RequestException as e:
            self.add_result(Result(
                title="SiYuan API Error",
                subtitle=f"An error occurred while calling SiYuan API: {e}",
                icon=ERROR
            ))
        except Exception as e:
            self.add_result(Result(
                title="Plugin Error",
                subtitle=f"An unexpected error occurred: {e}",
                icon=ERROR
            ))

        return self.return_results()