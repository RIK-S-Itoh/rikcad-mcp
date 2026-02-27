# rikcad-mcp

`rikcad-mcp` is a framework that runs an **MCP server** for **RIKCAD**.  
It uses the **Tapir** add-on with its additional JSON commands to let MCP clients like **Anthropic’s Claude** interact with RIKCAD.


## Installation

### Tapir

For `rikcad-mcp` to work, the [Tapir RIKCAD Add-On](https://github.com/tlorantfy/tapir-archicad-automation) is required. Please follow the installation instructions provided in that repository.

This package also depends on two Tapir files that define the JSON command structure used to automatically compile MCP-ready tools:

- [Tapir Command Definitions file](https://github.com/ENZYME-APD/tapir-archicad-automation/blob/main/docs/archicad-addon/command_definitions.js)  
- [Tapir Common Schema Definitions file](https://github.com/ENZYME-APD/tapir-archicad-automation/blob/main/docs/archicad-addon/common_schema_definitions.js)  

These files are located under the `src/mcp_server/tapir` folder.  
If you encounter mismatched commands, update the files directly from the Tapir repository.
These files can also be linked directly from the Tapir repo, but may cause mismatches if not updated in sync with the add-on.


### FastMCP Server

#### 1. Clone the repository
```bash
git clone https://github.com/lgradisar/archicad-mcp.git rikcad-mcp
cd rikcad-mcp
```

#### 2. Setup virtual environemnt
It is recommended to use [`uv`](https://docs.astral.sh/uv/getting-started/installation/) to install and create virutal environment.

Simply run:

```bash
uv sync
```

#### 3. Add to Claude config
Edit the config file manually:
- On Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- On Mac: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

Add this block (replace `YOUR_DIRECTORY` with the full path to rikcad-mcp):

```json
{
  "mcpServers": {
    "rikcad-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "YOUR_DIRECTORY/rikcad-mcp",
        "python",
        "-m",
        "server"
      ],
      "env": {
        "PYTHONPATH": "YOUR_DIRECTORY/rikcad-mcp/src"
      }
    }
  }
}
```


## Supported Tools

### Tapir JSON Commands
See the full list of [Tapir JSON Commands](https://enzyme-apd.github.io/tapir-archicad-automation/archicad-addon/).

### Custom Tools
This repository also supports adding your custom tools, either from the [official JSON commands](https://archicadapi.graphisoft.com/JSONInterfaceDocumentation/#Introduction) or other sources.  
They can be defined in the `src/mcp_server/tools/custom_tools.py` file.

For new RIKCAD-specific commands that are not part of the official JSON commands, it is recommended to contribute them directly to the Tapir repository instead.





