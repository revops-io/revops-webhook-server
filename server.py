from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def deal_activated():
  """ Get flags from deal activation """
  # Create a response object from the webhook's json
  response = request.get_json()

  # Get the deal
  deal = response.get('deal', {})
  status = deal.get('status', None)
  _id = deal.get('id', None)
  flags = deal.get('feature_flags', [])
  skus = deal.get('skus', [])
  terms = deal.get('terms', [])
  
  print("[{}] Deal webhook received for status={}".format(_id, status))

  for flag in flags:
    name = flag.get('name')
    enabled = flag.get('enabled', False)
    if enabled == True:
      print("Enabling FeatureFlag: {}".format(name))

  for sku in skus:
    title = sku.get('title')
    monthly_price = sku.get('monthly_price', "0.00")
    monthly_currency = sku.get('monthly_price_currency', "USD")

    # salesforce product/pricebook
    monthly_price = sku.get('pricebook_id', "")
    monthly_currency = sku.get('product_id', "")
    
    print("Customer purchased: {} for {} {}".format(
      title,
      monthly_price,
      monthly_currency,
    ))

  for term in terms:
    title = term.get('friendly_name')
    description = term.get('description')
    _id = term.get('id')
    term_value = term.get('value', None)

    print("Term included: {} [{}] = value: {}\Term description: {}".format(
      title,
      _id,
      term_value,
      description,
    ))

  return 'received!', 200

if __name__ == "__main__":
  app.run(debug=True, port=3005)
