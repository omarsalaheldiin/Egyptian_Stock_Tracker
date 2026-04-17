import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sys
from pathlib import Path
from data_manager import DataManager

class StockTrackerApp:
    """Main application for tracking Egyptian stock market positions and recommendations"""
    
    # Color scheme - Professional and colorful
    PRIMARY_COLOR = "#1e3a8a"      # Deep blue
    SECONDARY_COLOR = "#2563eb"    # Bright blue
    SUCCESS_COLOR = "#10b981"      # Green
    WARNING_COLOR = "#f59e0b"      # Amber
    DANGER_COLOR = "#ef4444"       # Red
    LIGHT_BG = "#f8fafc"           # Light slate
    DARK_TEXT = "#1e293b"          # Dark slate
    BORDER_COLOR = "#cbd5e1"       # Light border
    
    def __init__(self, root):
        self.root = root
        self.root.title("Egyptian Stock Tracker")
        self.root.geometry("1400x800")
        self.root.configure(bg=self.LIGHT_BG)
        
        # Initialize data manager
        self.data_manager = DataManager("data")
        
        # Configure styles
        self._configure_styles()
        
        # Create main notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create tabs
        self.portfolio_frame = ttk.Frame(self.notebook)
        self.watchlist_frame = ttk.Frame(self.notebook)
        self.summary_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.portfolio_frame, text="Portfolio Management")
        self.notebook.add(self.watchlist_frame, text="Watchlist Management")
        self.notebook.add(self.summary_frame, text="Summary")
        
        # Initialize each tab
        self._create_portfolio_tab()
        self._create_watchlist_tab()
        self._create_summary_tab()
    
    def _configure_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors for different elements
        style.configure('Title.TLabel', font=('Segoe UI', 14, 'bold'), background=self.LIGHT_BG, foreground=self.PRIMARY_COLOR)
        style.configure('Header.TLabel', font=('Segoe UI', 11, 'bold'), background=self.LIGHT_BG, foreground=self.DARK_TEXT)
        style.configure('Normal.TLabel', font=('Segoe UI', 10), background=self.LIGHT_BG, foreground=self.DARK_TEXT)
        
        style.configure('Treeview', font=('Segoe UI', 10), rowheight=25, background='white', fieldbackground='white')
        style.configure('Treeview.Heading', font=('Segoe UI', 10, 'bold'), background=self.PRIMARY_COLOR, foreground='white')
        style.map('Treeview.Heading', background=[('active', self.SECONDARY_COLOR)])
        
        style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'))
        style.configure('TButton', font=('Segoe UI', 10))
        style.configure('TEntry', font=('Segoe UI', 10))
        style.configure('TCombobox', font=('Segoe UI', 10))
    
    # ==================== PORTFOLIO TAB ====================
    
    def _create_portfolio_tab(self):
        """Create the portfolio management tab"""
        main_container = ttk.Frame(self.portfolio_frame)
        main_container.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Title
        title = ttk.Label(main_container, text="📈 Portfolio Management", style='Title.TLabel')
        title.pack(anchor="w", pady=(0, 15))
        
        # Input section
        input_frame = ttk.LabelFrame(main_container, text="Add/Update Stock", padding=10)
        input_frame.pack(fill="x", pady=(0, 15))
        
        ttk.Label(input_frame, text="Stock Name:", style='Header.TLabel').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.portfolio_stock_name = ttk.Entry(input_frame, width=30)
        self.portfolio_stock_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(input_frame, text="Amount (EGP):", style='Header.TLabel').grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.portfolio_amount = ttk.Entry(input_frame, width=20)
        self.portfolio_amount.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
        
        add_btn = ttk.Button(input_frame, text="✚ Add/Update", command=self._add_portfolio_stock)
        add_btn.grid(row=0, column=4, padx=10, pady=5)
        
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)
        
        # Tree view section
        tree_frame = ttk.LabelFrame(main_container, text="Your Holdings", padding=10)
        tree_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        columns = ('Stock Name', 'Amount (EGP)')
        self.portfolio_tree = ttk.Treeview(tree_frame, columns=columns, height=15, show='headings')
        
        self.portfolio_tree.column('Stock Name', width=300, anchor='w')
        self.portfolio_tree.column('Amount (EGP)', width=200, anchor='e')
        
        self.portfolio_tree.heading('Stock Name', text='Stock Name')
        self.portfolio_tree.heading('Amount (EGP)', text='Amount (EGP)')
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.portfolio_tree.yview)
        self.portfolio_tree.configure(yscroll=scrollbar.set)
        
        self.portfolio_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill="x")
        
        ttk.Button(button_frame, text="🗑️ Delete Selected", command=self._delete_portfolio_stock).pack(side="left", padx=5)
        ttk.Button(button_frame, text="🔄 Refresh", command=self._refresh_portfolio_tab).pack(side="left", padx=5)
        
        self._refresh_portfolio_tab()
    
    def _add_portfolio_stock(self):
        """Add or update a portfolio stock"""
        stock_name = self.portfolio_stock_name.get().strip()
        amount_str = self.portfolio_amount.get().strip()
        
        if not stock_name or not amount_str:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a valid positive number")
            return
        
        self.data_manager.add_portfolio_stock(stock_name, amount)
        messagebox.showinfo("Success", f"Stock '{stock_name}' added/updated successfully")
        self.portfolio_stock_name.delete(0, tk.END)
        self.portfolio_amount.delete(0, tk.END)
        self._refresh_portfolio_tab()
    
    def _delete_portfolio_stock(self):
        """Delete selected portfolio stock"""
        selection = self.portfolio_tree.selection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a stock to delete")
            return
        
        item = self.portfolio_tree.item(selection[0])
        stock_name = item['values'][0]
        
        if messagebox.askyesno("Confirm Delete", f"Delete stock '{stock_name}'?"):
            self.data_manager.delete_portfolio_stock(stock_name)
            messagebox.showinfo("Success", "Stock deleted successfully")
            self._refresh_portfolio_tab()
    
    def _refresh_portfolio_tab(self):
        """Refresh portfolio tree view"""
        for item in self.portfolio_tree.get_children():
            self.portfolio_tree.delete(item)
        
        stocks = self.data_manager.get_all_portfolio_stocks()
        for stock in sorted(stocks, key=lambda x: x['stock_name']):
            self.portfolio_tree.insert('', 'end', values=(stock['stock_name'], f"{stock['amount_egp']:,.2f}"))
    
    # ==================== WATCHLIST TAB ====================
    
    def _create_watchlist_tab(self):
        """Create the watchlist management tab"""
        main_container = ttk.Frame(self.watchlist_frame)
        main_container.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Title
        title = ttk.Label(main_container, text="⭐ Watchlist Management", style='Title.TLabel')
        title.pack(anchor="w", pady=(0, 15))
        
        # Create new watchlist section
        create_frame = ttk.LabelFrame(main_container, text="Create New Watchlist", padding=10)
        create_frame.pack(fill="x", pady=(0, 15))
        
        ttk.Label(create_frame, text="Watchlist Name:", style='Header.TLabel').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.new_watchlist_name = ttk.Entry(create_frame, width=40)
        self.new_watchlist_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Button(create_frame, text="✚ Create", command=self._create_watchlist).grid(row=0, column=2, padx=10, pady=5)
        create_frame.columnconfigure(1, weight=1)
        
        # Watchlist selection and management
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        # Left side - Watchlist list
        left_frame = ttk.LabelFrame(content_frame, text="Watchlists", padding=10)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        self.watchlist_listbox = tk.Listbox(left_frame, font=('Segoe UI', 10), height=15, bg='white')
        self.watchlist_listbox.pack(side="left", fill="both", expand=True)
        self.watchlist_listbox.bind('<<ListboxSelect>>', self._on_watchlist_selected)
        
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=self.watchlist_listbox.yview)
        self.watchlist_listbox.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        # Right side - Watchlist items
        right_frame = ttk.LabelFrame(content_frame, text="Stocks in Selected Watchlist", padding=10)
        right_frame.pack(side="right", fill="both", expand=True)
        
        # Add stock section
        add_stock_frame = ttk.Frame(right_frame)
        add_stock_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(add_stock_frame, text="Stock Name:", style='Header.TLabel').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.watchlist_stock_name = ttk.Entry(add_stock_frame, width=20)
        self.watchlist_stock_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        ttk.Label(add_stock_frame, text="Status:", style='Header.TLabel').grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.watchlist_status = ttk.Combobox(add_stock_frame, values=['Buy', 'Hold', 'Take Profit', 'Invest'], state='readonly', width=15)
        self.watchlist_status.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
        
        ttk.Button(add_stock_frame, text="✚ Add", command=self._add_watchlist_item).grid(row=0, column=4, padx=10, pady=5)
        add_stock_frame.columnconfigure(1, weight=1)
        add_stock_frame.columnconfigure(3, weight=1)
        
        # Watchlist items tree
        columns = ('Stock Name', 'Status')
        self.watchlist_items_tree = ttk.Treeview(right_frame, columns=columns, height=15, show='headings')
        
        self.watchlist_items_tree.column('Stock Name', width=200, anchor='w')
        self.watchlist_items_tree.column('Status', width=150, anchor='w')
        
        self.watchlist_items_tree.heading('Stock Name', text='Stock Name')
        self.watchlist_items_tree.heading('Status', text='Status')
        
        scrollbar2 = ttk.Scrollbar(right_frame, orient="vertical", command=self.watchlist_items_tree.yview)
        self.watchlist_items_tree.configure(yscroll=scrollbar2.set)
        
        self.watchlist_items_tree.pack(side="left", fill="both", expand=True)
        scrollbar2.pack(side="right", fill="y")
        
        # Buttons
        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill="x")
        
        ttk.Button(button_frame, text="🗑️ Delete Selected Item", command=self._delete_watchlist_item).pack(side="left", padx=5)
        ttk.Button(button_frame, text="🗑️ Delete Watchlist", command=self._delete_watchlist).pack(side="left", padx=5)
        ttk.Button(button_frame, text="🔄 Refresh", command=self._refresh_watchlist_tab).pack(side="left", padx=5)
        
        self._refresh_watchlist_tab()
    
    def _create_watchlist(self):
        """Create a new watchlist"""
        name = self.new_watchlist_name.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter a watchlist name")
            return
        
        self.data_manager.create_watchlist(name)
        messagebox.showinfo("Success", f"Watchlist '{name}' created successfully")
        self.new_watchlist_name.delete(0, tk.END)
        self._refresh_watchlist_tab()
    
    def _on_watchlist_selected(self, event):
        """Handle watchlist selection"""
        self._refresh_watchlist_items()
    
    def _add_watchlist_item(self):
        """Add a stock to the selected watchlist"""
        selection = self.watchlist_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a watchlist first")
            return
        
        watchlist_data = self.watchlist_listbox.get(selection[0])
        watchlist_id = watchlist_data.split(' (ID: ')[1].rstrip(')')
        
        stock_name = self.watchlist_stock_name.get().strip()
        status = self.watchlist_status.get()
        
        if not stock_name or not status:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        self.data_manager.add_watchlist_item(watchlist_id, stock_name, status)
        messagebox.showinfo("Success", f"Stock '{stock_name}' added to watchlist")
        self.watchlist_stock_name.delete(0, tk.END)
        self.watchlist_status.set('')
        self._refresh_watchlist_items()
    
    def _delete_watchlist_item(self):
        """Delete selected item from watchlist"""
        selection = self.watchlist_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a watchlist first")
            return
        
        item_selection = self.watchlist_items_tree.selection()
        if not item_selection:
            messagebox.showwarning("Selection Error", "Please select a stock to delete")
            return
        
        watchlist_data = self.watchlist_listbox.get(selection[0])
        watchlist_id = watchlist_data.split(' (ID: ')[1].rstrip(')')
        
        item = self.watchlist_items_tree.item(item_selection[0])
        stock_name = item['values'][0]
        
        if messagebox.askyesno("Confirm Delete", f"Delete '{stock_name}' from watchlist?"):
            self.data_manager.delete_watchlist_item(watchlist_id, stock_name)
            messagebox.showinfo("Success", "Stock deleted from watchlist")
            self._refresh_watchlist_items()
    
    def _delete_watchlist(self):
        """Delete a watchlist"""
        selection = self.watchlist_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selection Error", "Please select a watchlist to delete")
            return
        
        watchlist_data = self.watchlist_listbox.get(selection[0])
        watchlist_name = watchlist_data.split(' (ID: ')[0]
        watchlist_id = watchlist_data.split(' (ID: ')[1].rstrip(')')
        
        if messagebox.askyesno("Confirm Delete", f"Delete watchlist '{watchlist_name}' and all its items?"):
            self.data_manager.delete_watchlist(watchlist_id)
            messagebox.showinfo("Success", "Watchlist deleted successfully")
            self._refresh_watchlist_tab()
    
    def _refresh_watchlist_tab(self):
        """Refresh watchlist tab"""
        self.watchlist_listbox.delete(0, tk.END)
        watchlists = self.data_manager.get_all_watchlists()
        for wl in sorted(watchlists, key=lambda x: x['watchlist_name']):
            self.watchlist_listbox.insert(tk.END, f"{wl['watchlist_name']} (ID: {wl['watchlist_id']})")
        
        self._refresh_watchlist_items()
    
    def _refresh_watchlist_items(self):
        """Refresh watchlist items tree"""
        for item in self.watchlist_items_tree.get_children():
            self.watchlist_items_tree.delete(item)
        
        selection = self.watchlist_listbox.curselection()
        if not selection:
            return
        
        watchlist_data = self.watchlist_listbox.get(selection[0])
        watchlist_id = watchlist_data.split(' (ID: ')[1].rstrip(')')
        
        items = self.data_manager.get_watchlist_items(watchlist_id)
        for item in sorted(items, key=lambda x: x['stock_name']):
            self.watchlist_items_tree.insert('', 'end', values=(item['stock_name'], item['status']))
    
    # ==================== SUMMARY TAB ====================
    
    def _create_summary_tab(self):
        """Create the summary tab"""
        main_container = ttk.Frame(self.summary_frame)
        main_container.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Title
        title = ttk.Label(main_container, text="📊 Summary & Analysis", style='Title.TLabel')
        title.pack(anchor="w", pady=(0, 15))
        
        # View options
        options_frame = ttk.LabelFrame(main_container, text="View Options", padding=10)
        options_frame.pack(fill="x", pady=(0, 15))
        
        self.summary_view_var = tk.StringVar(value="full")
        ttk.Radiobutton(options_frame, text="View Full Summary (All Stocks)", variable=self.summary_view_var, 
                       value="full", command=self._refresh_summary_tab).pack(side="left", padx=10)
        ttk.Radiobutton(options_frame, text="View Individual Watchlist", variable=self.summary_view_var, 
                       value="watchlist", command=self._on_summary_view_changed).pack(side="left", padx=10)
        
        # Watchlist selector frame
        self.summary_watchlist_frame = ttk.Frame(options_frame)
        self.summary_watchlist_frame.pack(side="left", padx=10)
        
        ttk.Label(self.summary_watchlist_frame, text="Select Watchlist:", style='Header.TLabel').pack(side="left", padx=5)
        self.summary_watchlist_combo = ttk.Combobox(self.summary_watchlist_frame, state='readonly', width=30)
        self.summary_watchlist_combo.pack(side="left", padx=5)
        self.summary_watchlist_combo.bind('<<ComboboxSelected>>', lambda e: self._refresh_summary_tab())
        
        self.summary_watchlist_frame.pack_forget()  # Hide initially
        
        # Summary tree view section
        tree_frame = ttk.LabelFrame(main_container, text="Stock Summary", padding=10)
        tree_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        self.summary_tree = ttk.Treeview(tree_frame, show='tree headings', height=20)
        self.summary_tree.pack(fill="both", expand=True, side="left")
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.summary_tree.yview)
        self.summary_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = ttk.Frame(main_container)
        button_frame.pack(fill="x")
        
        ttk.Button(button_frame, text="🔄 Refresh", command=self._refresh_summary_tab).pack(side="left", padx=5)
        
        self._refresh_summary_tab()
    
    def _on_summary_view_changed(self):
        """Handle summary view change"""
        if self.summary_view_var.get() == "watchlist":
            self.summary_watchlist_frame.pack(side="left", padx=10)
            self._populate_summary_watchlist_combo()
        else:
            self.summary_watchlist_frame.pack_forget()
        
        self._refresh_summary_tab()
    
    def _populate_summary_watchlist_combo(self):
        """Populate the watchlist combo box"""
        watchlists = self.data_manager.get_all_watchlists()
        watchlist_names = [w['watchlist_name'] for w in sorted(watchlists, key=lambda x: x['watchlist_name'])]
        self.summary_watchlist_combo['values'] = watchlist_names
        if watchlist_names:
            self.summary_watchlist_combo.set(watchlist_names[0])
    
    def _refresh_summary_tab(self):
        """Refresh the summary view"""
        # Clear existing tree
        for item in self.summary_tree.get_children():
            self.summary_tree.delete(item)
        
        # Set column structure based on view type
        if self.summary_view_var.get() == "full":
            self._show_full_summary()
        else:
            self._show_watchlist_summary()
    
    def _show_full_summary(self):
        """Show summary for all stocks"""
        # Get all data
        portfolio_stocks = {s['stock_name']: s['amount_egp'] for s in self.data_manager.get_all_portfolio_stocks()}
        stocks_with_watchlists = self.data_manager.get_all_stocks_with_watchlists()
        watchlists_dict = {w['watchlist_id']: w['watchlist_name'] for w in self.data_manager.get_all_watchlists()}
        
        # Set columns dynamically
        watchlist_ids = set()
        for stock_data in stocks_with_watchlists.values():
            for wl_id, _, _ in stock_data:
                watchlist_ids.add(wl_id)
        
        sorted_watchlist_ids = sorted(watchlist_ids, key=lambda x: watchlists_dict.get(x, ''))
        
        columns = ['Stock Name'] + [watchlists_dict[wl_id] for wl_id in sorted_watchlist_ids] + ['Total Positions', 'Portfolio Amount (EGP)', 'Portfolio Status']
        
        self.summary_tree['columns'] = columns
        self.summary_tree.column('#0', width=0, stretch=tk.NO)
        
        for col in columns:
            self.summary_tree.column(col, anchor='w', width=150)
            self.summary_tree.heading(col, text=col, anchor='w')
        
        # Populate data
        all_stocks = sorted(set(list(portfolio_stocks.keys()) + list(stocks_with_watchlists.keys())))
        
        for stock_name in all_stocks:
            row = [stock_name]
            watchlist_data = stocks_with_watchlists.get(stock_name, [])
            
            total_positions = 0
            for wl_id in sorted_watchlist_ids:
                statuses = [status for w_id, _, status in watchlist_data if w_id == wl_id]
                if statuses:
                    row.append(f"{', '.join(statuses)} (1x)")
                    total_positions += 1
                else:
                    row.append('-')
            
            position_egp = total_positions * 10000
            portfolio_amount = portfolio_stocks.get(stock_name, 0)
            
            if portfolio_amount > 0:
                status = "✓ Matched" if abs(portfolio_amount - position_egp) < 1 else f"Mismatch: {portfolio_amount:,.0f} vs {position_egp:,.0f}"
            else:
                status = "Not in Portfolio" if position_egp > 0 else "-"
            
            row.extend([total_positions, f"{portfolio_amount:,.2f}", status])
            
            # Insert with alternating colors
            tag = 'oddrow' if len(self.summary_tree.get_children()) % 2 == 0 else 'evenrow'
            self.summary_tree.insert('', tk.END, values=tuple(row), tags=(tag,))
        
        # Configure tags for alternating colors
        self.summary_tree.tag_configure('oddrow', background='#f8fafc')
        self.summary_tree.tag_configure('evenrow', background='#e8ecf1')
    
    def _show_watchlist_summary(self):
        """Show summary for a specific watchlist"""
        selected_watchlist = self.summary_watchlist_combo.get()
        if not selected_watchlist:
            return
        
        # Find watchlist ID
        watchlists = self.data_manager.get_all_watchlists()
        watchlist_id = None
        for wl in watchlists:
            if wl['watchlist_name'] == selected_watchlist:
                watchlist_id = wl['watchlist_id']
                break
        
        if not watchlist_id:
            return
        
        # Get data
        portfolio_stocks = {s['stock_name']: s['amount_egp'] for s in self.data_manager.get_all_portfolio_stocks()}
        watchlist_items = self.data_manager.get_watchlist_items(watchlist_id)
        
        # Set columns
        columns = ['Stock Name', 'Status', 'Position Size (EGP)', 'Your Position (EGP)', 'Variance']
        self.summary_tree['columns'] = columns
        self.summary_tree.column('#0', width=0, stretch=tk.NO)
        
        for col in columns:
            self.summary_tree.column(col, anchor='w', width=150)
            self.summary_tree.heading(col, text=col, anchor='w')
        
        # Populate data
        for item in sorted(watchlist_items, key=lambda x: x['stock_name']):
            stock_name = item['stock_name']
            status = item['status']
            position_egp = 10000
            portfolio_amount = portfolio_stocks.get(stock_name, 0)
            variance = portfolio_amount - position_egp
            
            row = [
                stock_name,
                status,
                f"{position_egp:,.2f}",
                f"{portfolio_amount:,.2f}",
                f"{variance:+,.2f}"
            ]
            
            # Color code by variance
            if portfolio_amount == position_egp:
                tag = 'match'
            elif portfolio_amount > position_egp:
                tag = 'over'
            elif portfolio_amount > 0:
                tag = 'under'
            else:
                tag = 'missing'
            
            self.summary_tree.insert('', tk.END, values=tuple(row), tags=(tag,))
        
        # Configure tags
        self.summary_tree.tag_configure('match', background=self.SUCCESS_COLOR, foreground='white')
        self.summary_tree.tag_configure('over', background='#dbeafe', foreground=self.DARK_TEXT)
        self.summary_tree.tag_configure('under', background='#fef3c7', foreground=self.DARK_TEXT)
        self.summary_tree.tag_configure('missing', background='#fee2e2', foreground=self.DARK_TEXT)


def main():
    root = tk.Tk()
    app = StockTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
