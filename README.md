# Example RevOps Webhook Server for Python

## How do RevOps Webhooks work?

On every change that occurs to a Deal in RevOps, a webhook request will be sent to the URL(s) configured in your RevOps account. This request will contain information about the event.

<img src="https://www.revops.io/resources/images/webhook_graphic.png" alt="Webhooks under the hood" width="750px"/>

URLs for webhooks are configured in your RevOps instance inside <a href="https://auth-anon.revops.io/integrations/webhooks/setup">`Settings > Webhook `</a>

> The following is a `python` example, but can be adapted to any language.

## Installation requirements

1. **ngrok** https://ngrok.com/download
2. **python** Python >=3.6 https://www.python.org/
3. **pip** https://github.com/pypa/pip


## Getting Started

For documentation on getting started check out our <a href="https://www.revops.io/docs/how-to/setup-webhooks">How-to Setup Webhooks</a> article.

To run the service, start by cloning the following project from GitHub.
```bash
$> git clone https://github.com/revops-io/revops-webhook-server
$> cd revops-webhook-server
$> pip install -r requirements.txt
$> python server.py
$> ngrok http 3005
```