import websocket
import json

#Market Streams of USD-M Futures

class Market_stream():
    
    def __init__(self):
        self.baseUrl = 'wss://fstream.binance.com/ws'
        
    def connect(self, param):
        def on_open(ws):
            subscribe_message = {"method": "SUBSCRIBE", "params":[param],"id": 1}
            ws.send(json.dumps(subscribe_message))
            
        def on_message(ws, message):
            print(json.loads(message))

        def on_close(ws):
            print("closed connection")

        ws = websocket.WebSocketApp(self.baseUrl, on_open=on_open, on_message=on_message, on_close=on_close)
        ws.run_forever()

    #Aggregate Trade Stream
    def Aggregate_Trade_Stream(self, symbol):
        self.connect(symbol+'@aggTrade')
        
    #Mark Price Stream
    def Mark_Price_Stream(self, symbol = None, freq=None):
        if(len(freq)):
            freq='@'+freq+'s'
        self.connect(symbol+'@markPrice'+freq)

    #Mark Price Stream for All market
    def Mark_Price_Stream(self, freq=None):
        if(len(freq)):
            freq='@'+freq+'s'
        self.connect('!markPrice@arr'+freq)

    #Kline/Candlestick Streams
    def Kline_Stream(self, symbol = None, interval = None):
        self.connect(symbol+'@kline_'+interval)
            
    #Continuous Contract Kline/Candlestick Streams
    def Continuous_Kline_Stream(self, pair = None, contractType = None, interval = None):
        self.connect(pair+'_'+contractType+'@continuous_Kline_'+interval)
            
    #Individual Symbol Mini Ticker Stream
    def Mini_Ticker_Stream(self, symbol = None):
        self.connect(symbol+'@miniTicker')

    #All Market Mini Tickers Stream
    def All_Mini_Ticker_Stream(self):
        self.connect('!miniTicker@arr')
            
    #Individual Symbol Ticker Streams
    def Ticker_Stream(self, symbol = None):
        self.connect(symbol+'@ticker')
            
    #All Market Tickers Stream
    def All_Mini_Ticker_Stream(self):
        self.connect('!ticker@arr')

    #Individual Symbol Book Ticker Streams
    def Book_Ticker_Streams(self, symbol = None):
        self.connect(symbol+'@bookTicker')
            
    #All Book Tickers Stream
    def All_Book_Ticker_Stream(self):
        self.connect('!bookTicker')
            
    #Liquidation Order Streams
    def Liquidation_Order_Streams(self, symbol = None):
        self.connect(symbol+'@forceOrder')
            
    #All Market Liquidation Order Streams
    def All_Market_Liquidation_Order_Stream(self):
        self.connect('!forceOrder@arr')

            
    #Partial Book Depth Streams
    def Partial_Book_Depth_Stream(self, symbol = None, levels = None, freq = None):
        if(len(freq)):
            freq='@'+freq+'ms'
        self.connect(symbol+'@depth'+levels+freq)
            
    #Diff. Book Depth Streams
    def Diff_Book_Depth_Stream(self, symbol = None, freq = None):
        if(len(freq)):
            freq='@'+freq+'ms'
        self.connect(symbol+'@depth'+freq)
            
    #Composite Index Symbol Information Streams
    def Composite_Index_Stream(self, symbol = None):
        self.connect(symbol+'@compositeIndex')
            
    #Contract Info Stream
    def Contract_Info_Stream(self):
        self.connect('!contractInfo')

