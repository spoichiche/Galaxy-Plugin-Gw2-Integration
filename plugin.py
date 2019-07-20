import sys
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform

class PluginGw2(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(
            Platform.gw2,
            "0.1",
            reader,
            writer,
            token
        )

    async def authenticate(self, stored_credentials=None):
        pass

def main():
    create_and_run_plugin(PluginGw2, sys.argv)

# run plugin event loop
if __name__ == "__main__":
    main()