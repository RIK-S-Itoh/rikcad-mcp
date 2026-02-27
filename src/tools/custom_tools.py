def init_tools(mcp):
    @mcp.tool(
        description="Test connection with RIKCAD"
    )
    def test_connection():
        """
        Example of custom tool definition with fastmcp
        """
        from archicad import ACConnection
        conn = ACConnection.connect()
        if conn is None:
            return "エラー: RIKCADに接続できません"

        acc = conn.commands
        act = conn.types
        
        
        return conn
