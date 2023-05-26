# py-bitcoin

Bitcoin related Python scripts. Will add to this over time.

## Current price and fees

The first script is a Python version of my [Bitcoin Price and Fees script](https://github.com/xannythepleb/go-bitcoin/blob/main/BitcoinPriceAndFees.go) from the [go-bitcoin repo.](https://github.com/xannythepleb/go-bitcoin)

Gives you a choice of five APIs to use for checking the current Bitcoin price in USD: CoinDesk, Coingecko, Bitfinex, Kraken, or Binance.

It produces an almost identical output with the exact same information:

```

Choose an API to fetch Bitcoin price:

1. CoinDesk
2. CoinGecko
3. Bitfinex
4. Kraken
5. Binance

Enter your choice (1, 2, 3, 4, or 5): 5

  1 BTC = $26,476
  1 BTC = 1 BTC

  The recommended tx fees are: 
   Fastest fee: 73 sats/vB
   Half hour fee: 62 sats/vB
   Hour fee: 52 sats/vB
   Economy fee: 30 sats/vB
   Minimum fee: 15 sats/vB

    #FreeRoss
   
```

## Transaction history for given wallet address

Uses the Mempool.space API to display transaction history related to any type of Bitcoin address including legacy, segwit, and taproot:

```

Enter a Bitcoin address (Legacy, Segwit, or Taproot): bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk

Transaction 1:
Hash: 1cf53772ec3ba217258d6ab2eab668d727d9765418d1dda1cc8e9c2e42b0bd42
Time: 1684120485
Inputs:
bc1q35ge2n8ujjknzuffugphqgvj9aafgwyjhsgwg5: 461506546 sats
Outputs:
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 187755 sats
bc1qs57z04t9fsn5tdfxqywttuzcrpsz9leelxgasw: 461315173 sats

Transaction 2:
Hash: 34e008db86744e7718626009de5a7f6ca07a7c26a3bcf2be0dbf6c90a9c57990
Time: 1684090679
Inputs:
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 356000000 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 1480856 sats
bc1qzpdm7vs4c485jffyldll7vngptfjp35au3ktx7: 1177917 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 3879000 sats
Outputs:
bc1qzpdm7vs4c485jffyldll7vngptfjp35au3ktx7: 1927935 sats
3696XJFswhwdh6PMi4yhDcHee3PWfHnCvb: 360600000 sats

Transaction 3:
Hash: 86b744c80d6eb94a29a2589e1bae9c7bbe63d555a400cc03513bd5411d45b057
Time: 1684085701
Inputs:
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 10020 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 2127 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 1478465 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 1383 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 700000 sats
bc1q202rwadss5k6phxjazugjp87ncjmt62szj0ylk: 38666 sats
Outputs:
bc1qzpdm7vs4c485jffyldll7vngptfjp35au3ktx7: 1177917 sats
3696XJFswhwdh6PMi4yhDcHee3PWfHnCvb: 1000000 sats

```
