# Flow.Launcher.Plugin.SiYuanSearch

A Flow Launcher plugin that lets you search your SiYuan notes and open them directly in SiYuan.

## Features
- Search your SiYuan blocks using SQL queries
- Open selected blocks directly in SiYuan using siyuan:// protocol
- Simple configuration of API URL and token

## Installation
1. Download the plugin
2. Extract it to your Flow Launcher plugins directory
3. Restart Flow Launcher

## Configuration
1. Open SiYuan and enable the API:
   - Go to Settings > API
   - Enable API service
   - Copy your API token

2. Configure the plugin in Flow Launcher:
   - Open Flow Launcher settings
   - Find SiYuan Search plugin
   - Set your SiYuan API URL (default: http://127.0.0.1:6806)
   - Paste your API token

## Usage
Type `sy` followed by your search query to search your SiYuan notes. Select a result to open it in SiYuan.

## Requirements
- SiYuan Note with API enabled
- Flow Launcher