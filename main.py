import customtkinter as ctk
from ApiClient import prices
from price_updater import start_price_thread

start_price_thread()


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("600x300")
        self.title("Crypto Coingecko")
        self.resizable(False, False)

        self.Frame3_Crypto = ctk.CTkFrame(self, width=270, height=50, fg_color="black")
        self.Frame3_Crypto.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")
        self.Frame3_Crypto.grid_propagate(False)

        self.Frame2_Crypto = ctk.CTkFrame(self, width=270, height=50, fg_color="black")
        self.Frame2_Crypto.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")
        self.Frame2_Crypto.grid_propagate(False)
        
        self.Frame1_Crypto = ctk.CTkFrame(self, width=270, height=50, fg_color="black")
        self.Frame1_Crypto.grid(row=0, column=1, padx=0, pady=90, sticky="nsew")
        self.Frame1_Crypto.grid_propagate(False)
        
        self.Frame_Crypto = ctk.CTkFrame(self, width=270, height=50, fg_color="black")
        self.Frame_Crypto.grid(row=0, column=0, padx=20, pady=90, sticky="nsew")
        self.Frame_Crypto.grid_propagate(False)
        
        self.Crypto_Label = ctk.CTkLabel(self, text="Crypto Coingecko", font=("Arial", 25, "bold"), width=500, height=40)
        self.Crypto_Label.place(x=45, y=10)
        
        self.Bitcoin_Label = ctk.CTkLabel(self, text="Bitcoin Tracker", font=("Arial", 20, "bold"))
        self.Bitcoin_Label.place(x=80, y=55)
        
        self.Ton_Label = ctk.CTkLabel(self, text="Ton Tracker", font=("Arial", 20, "bold"))
        self.Ton_Label.place(x=400, y=55)
        
        self.Binance_Label = ctk.CTkLabel(self, text="Binance Tracker", font=("Arial", 20, "bold"))
        self.Binance_Label.place(x=80, y=200)
        
        self.Eth_Label = ctk.CTkLabel(self, text="Ethereum", font=("Arial", 20, "bold"))
        self.Eth_Label.place(x=410, y=200)
        
        self.Price_Bitcoin = ctk.CTkLabel(self.Frame_Crypto, text="Price Bitcoin: ", font=("Arial", 20, "bold"))
        self.Price_Bitcoin.place(x=10, y=10)
        
        self.Price_Binance = ctk.CTkLabel(self.Frame2_Crypto, text="Price Binance: ", font=("Arial", 20, "bold"))
        self.Price_Binance.place(x=10, y=10)
        
        self.Price_Etherneum = ctk.CTkLabel(self.Frame3_Crypto, text="Price Ethereum: ", font=("Arial", 20, "bold"))
        self.Price_Etherneum.place(x=10, y=10)
        
        self.Price_TON = ctk.CTkLabel(self.Frame1_Crypto, text="Price Ethereum: ", font=("Arial", 20, "bold"))
        self.Price_TON.place(x=10, y=10)
        
        self.update()
        
    def update(self):
        btc_price = prices.get("BTCUSDT", "reload...")
        eth_price = prices.get("ETHUSDT", "reload...")
        bnb_price = prices.get("BNBUSDT", "reload...")
        ton_price = prices.get("TONUSDT", "reload...")
        
        btc_text = (f"${btc_price:,.2f}" if isinstance(btc_price, (int, float)) else btc_price)
        eth_text = (f"${eth_price:,.2f}" if isinstance(eth_price, (int, float)) else eth_price)
        bnb_text = (f"${bnb_price:,.2f}" if isinstance(bnb_price, (int, float)) else bnb_price)
        ton_text = (f"${ton_price:,.2f}" if isinstance(ton_price, (int, float)) else ton_price)
        
        self.Price_Bitcoin.configure(text=f"Price Bitcoin: {btc_text}")
        self.Price_Etherneum.configure(text=f"Price Ethereum: {eth_text}")
        self.Price_Binance.configure(text=f"Price Binance: {bnb_text}")       
        self.Price_TON.configure(text=f"Price TON: {ton_text}")
                
        self.after(1000, self.update)

app = App()
app.mainloop()