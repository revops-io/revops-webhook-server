# How to setup your first webhook?
Connecting your business to RevOps is exciting and helps unlock new opportunities for automation.

We use a simple example to show how `deal-activated` events can be used to enable feature flags. It is a simple application but demonstrates the power webhooks.

With this guide, you will:

1. Create a webhook endpoint.
2. Utilize information from a Deal.
3. Have fun!

## Under the Hood

With every change to a **Deal** in RevOps, a `webhook` of a specific type will be sent. Where we send it is up to you and can be defined in RevOps.

URLs for webhooks are configured in your RevOps instance inside `/settings`.

## Step 1: Create an endpoint to respond to activated deals.

Get started by cloning the following project from Github.
```bash
$> git clone revops-webhook-server
$> cd revops-webhook-server
$> python server.py
$> ngrok
```

Start with `server.py`, which uses [Flask](http://flask.pocoo.org/)   to handle a JSON POST request.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/deals/activated", methods=['POST'])
def deal_activated():
    """ Get flags from deal activation """
    # Create a response object from the webhook's json
    response = request.get_json()

    # Get the deal
    deal = response.get('deal', {})
    flags = deal.get('feature_flags', [])

    for flag in flags:
      name = flag.get('name')
      enabled = flag.get('enabled', False)
      if enabled === True:
        print(f"Enabling FeatureFlag {name}")

    return 'received!', 200

if __name__ == "__main__":
    app.run(debug=True, port=3005)
```


## Step 2: Connect your service to RevOps.

1. As an administrator, log in to your RevOps account.
2. Visit `/settings/webhooks`
3. Create a new webhook endpoint, and set the public facing ngrok url.
4. Click the Test button.

## Step 3: Error handling

Let's extend the `server.py` example a bit to handle errors when communicating to your own feature flag service.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/deals/activated", methods=['POST'])
def deal_activated():
    """ Get flags from deal activation """
    # Create a response object from the webhook's json
    response = request.get_json()

    # Get the deal
    deal = response.get('deal', {})
    flags = deal.get('feature_flags', [])

    try:
      for flag in flags:
        name = flag.get('name')
        enabled = flag.get('enabled', False)
        if enabled === True:
          print(f"Enabling FeatureFlag {name}")
          raise Exception("A problem occurred setting a flag")
    except Exception as e:
      print('An error occurred trying to set flags')
      print(e)
      # Return 500 will tell RevOps to retry requests
      return str(e), 500

    return 'received!', 200

if __name__ == "__main__":
    app.run(debug=True, port=3005)
```
