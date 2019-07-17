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
      if enabled == True:
        print(f"Enabling FeatureFlag {name}")

    return 'received!', 200

if __name__ == "__main__":
    app.run(debug=True, port=3005)