import tkinter as tk
from tkinter import ttk, messagebox
import converter_engine as ce

class ElectricalConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BEEE Electrical Unit Converter")
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        
        # Link UI category strings to engine dictionaries
        self.categories = {
            "Voltage": ce.VOLTAGE_UNITS,
            "Current": ce.CURRENT_UNITS,
            "Power": ce.POWER_UNITS,
            "Energy": ce.ENERGY_UNITS
        }
        
        self.create_widgets()

    def create_widgets(self):
        # 1. Main Title Header
        tk.Label(self.root, text="Electrical Unit Converter", font=("Arial", 16, "bold"), fg="#1a73e8").pack(pady=10)
        
        # 2. Category Selection Dropdown
        tk.Label(self.root, text="Select Category:", font=("Arial", 10)).pack()
        self.category_var = tk.StringVar(value="Voltage")
        self.category_menu = ttk.Combobox(self.root, textvariable=self.category_var, values=list(self.categories.keys()), state="readonly")
        self.category_menu.pack(pady=5)
        self.category_menu.bind("<<ComboboxSelected>>", self.update_units)
        
        # 3. Numeric Value Entry Field
        tk.Label(self.root, text="Enter Value:", font=("Arial", 10)).pack()
        self.input_entry = ttk.Entry(self.root, width=23)
        self.input_entry.pack(pady=5)
        
        # 4. Horizontal Layout Frame for unit selection
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        
        # "From Unit" Menu
        tk.Label(frame, text="From:").grid(row=0, column=0, padx=5)
        self.from_unit_var = tk.StringVar()
        self.from_menu = ttk.Combobox(frame, textvariable=self.from_unit_var, width=8, state="readonly")
        self.from_menu.grid(row=0, column=1, padx=5)
        
        # "To Unit" Menu
        tk.Label(frame, text="To:").grid(row=0, column=2, padx=5)
        self.to_unit_var = tk.StringVar()
        self.to_menu = ttk.Combobox(frame, textvariable=self.to_unit_var, width=8, state="readonly")
        self.to_menu.grid(row=0, column=3, padx=5)
        
        # Initialize dropdown units dynamically based on category
        self.update_units() 
        
        # 5. Conversion Trigger Button
        self.btn_convert = ttk.Button(self.root, text="Convert", command=self.perform_conversion)
        self.btn_convert.pack(pady=10)
        
        # 6. Results Display Label
        self.result_label = tk.Label(self.root, text="Result: --", font=("Arial", 12, "bold"), fg="#202124")
        self.result_label.pack(pady=10)

    def update_units(self, event=None):
        """Changes the dropdown options automatically when you pick a new category."""
        category = self.category_var.get()
        units = list(self.categories[category].keys())
        self.from_menu['values'] = units
        self.to_menu['values'] = units
        self.from_menu.current(1) # Defaults to the standard Base Unit (e.g., V, A, W, Wh)
        self.to_menu.current(0)

    def perform_conversion(self):
        """Validates inputs, calls the engine math function, and shows results."""
        try:
            val = float(self.input_entry.get())
            cat = self.category_var.get()
            f_unit = self.from_unit_var.get()
            t_unit = self.to_unit_var.get()
            
            # Request conversion value from our engine module
            res = ce.convert_units(val, f_unit, t_unit, self.categories[cat])
            self.result_label.config(text=f"Result: {val} {f_unit} = {res:.4f} {t_unit}")
        except ValueError:
            messagebox.showerror("Input Error", "Please type a valid numeric number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectricalConverterApp(root)
    root.mainloop()