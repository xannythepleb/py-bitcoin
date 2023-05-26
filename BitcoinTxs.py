import requests
import json

def get_transactions_mempool(bitcoin_address):
    URL = f"https://mempool.space/api/address/{bitcoin_address}/txs"
    response = requests.get(URL)
    if response.status_code == 200:
        transactions = json.loads(response.text)
        return transactions
    else:
        print("Unable to fetch transactions from Mempool.space.")
        return None

def print_transactions(transactions):
    if transactions:
        for i, transaction in enumerate(transactions):
            print(f"\nTransaction {i+1}:")
            print(f"Hash: {transaction['txid']}")
            print(f"Time: {transaction['status']['block_time']}")
            print("Inputs:")
            for input in transaction['vin']:
                print(f"{input['prevout']['scriptpubkey_address']}: {input['prevout']['value']} sats")
            print("Outputs:")
            for output in transaction['vout']:
                print(f"{output['scriptpubkey_address']}: {output['value']} sats")
    else:
        print("No transactions to display.")

if __name__ == "__main__":
    bitcoin_address = input("\nEnter a Bitcoin address (Legacy, Segwit, or Taproot): ")
    transactions = get_transactions_mempool(bitcoin_address)

    print_transactions(transactions)
