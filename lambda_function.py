import json


def lambda_handler(event, context):
    """
    AWS Lambda handler for processing a name submitted by the frontend.

    Args:
        event: Request event from API Gateway.
        context: AWS Lambda runtime information.

    Returns:
        dict: HTTP response containing a greeting message.
    """

    try:
        body = event.get("body")

        if isinstance(body, str):
            body = json.loads(body)
        elif not isinstance(body, dict):
            body = {}

        name = body.get("name", "Guest").strip()

        if not name:
            name = "Guest"

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": f"Hello, {name}! This response is from AWS Lambda."
            })
        }

    except (json.JSONDecodeError, AttributeError, TypeError):
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Invalid request. Please provide a valid name."
            })
        }
