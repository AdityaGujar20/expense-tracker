import argparse

from fastapi import FastAPI
from fastmcp import FastMCP
import uvicorn

from app.api.routes.transactions import router


app = FastAPI()

app.include_router(router=router)

mcp = FastMCP.from_fastapi(
    app = app
)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--api",
        action="store_true",
        help="Run the FastAPI server"
    )

    parser.add_argument(
        "--mcp",
        action="store_true",
        help="Run the MCP server"
    )

    args = parser.parse_args()

    if args.api:
        uvicorn.run(
            app=app,
            host="0.0.0.0",
            port=8080
        )

    elif args.mcp:
        mcp.run(
            transport="http",
            host="0.0.0.0",
            port=9000
        )

    else:
        parser.error("Specify either --api or --mcp")
