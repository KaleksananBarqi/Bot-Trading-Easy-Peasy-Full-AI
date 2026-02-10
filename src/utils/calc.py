from typing import Dict, Any
import config


def validate_ai_setup(
    entry_price: float,
    tp_price: float, 
    sl_price: float,
    side: str,
    current_price: float,
    atr: float,
    min_rr_ratio: float = 1.0
) -> Dict[str, Any]:
    """
    Validasi apakah setup dari AI masuk akal secara matematis.
    
    Returns:
        {
            "is_valid": bool,
            "errors": [],
            "warnings": [],
            "risk_reward": float
        }
    """
    errors = []
    warnings = []
    
    # 1. Basic validation
    if entry_price <= 0 or tp_price <= 0 or sl_price <= 0:
        errors.append("Entry/TP/SL must be greater than 0")
        return {"is_valid": False, "errors": errors, "warnings": warnings, "risk_reward": 0}
    
    # 2. Direction validation
    if side.lower() == 'buy':
        if tp_price <= entry_price:
            errors.append(f"BUY: TP ({tp_price}) must be > Entry ({entry_price})")
        if sl_price >= entry_price:
            errors.append(f"BUY: SL ({sl_price}) must be < Entry ({entry_price})")
    else:  # sell/short
        if tp_price >= entry_price:
            errors.append(f"SELL: TP ({tp_price}) must be < Entry ({entry_price})")
        if sl_price <= entry_price:
            errors.append(f"SELL: SL ({sl_price}) must be > Entry ({entry_price})")
    
    if errors:
        return {"is_valid": False, "errors": errors, "warnings": warnings, "risk_reward": 0}
    
    # 3. Calculate R:R
    risk = abs(entry_price - sl_price)
    reward = abs(tp_price - entry_price)
    rr_ratio = reward / risk if risk > 0 else 0
    
    # 4. R:R validation
    if rr_ratio < min_rr_ratio:
        errors.append(f"Risk:Reward ({rr_ratio:.2f}) below minimum ({min_rr_ratio})")
    
    # 5. Extreme distance check (SL > 10% from entry = suspicious)
    sl_distance_pct = abs(entry_price - sl_price) / entry_price
    if sl_distance_pct > 0.10:
        warnings.append(f"SL very far from entry ({sl_distance_pct*100:.1f}%). Double check AI logic.")
    
    is_valid = len(errors) == 0
    
    return {
        "is_valid": is_valid,
        "errors": errors,
        "warnings": warnings,
        "risk_reward": round(rr_ratio, 2)
    }


def calculate_profit_loss_estimation(
    entry_price: float,
    tp_price: float,
    sl_price: float,
    side: str,
    amount_usdt: float,
    leverage: int
) -> Dict[str, float]:
    """
    Menghitung estimasi profit dan loss dalam USDT dan persentase ROI.
    
    Args:
        entry_price (float): Harga entry.
        tp_price (float): Harga Take Profit.
        sl_price (float): Harga Stop Loss.
        side (str): 'buy' atau 'sell'.
        amount_usdt (float): Margin yang digunakan (USDT).
        leverage (int): Leverage yang dipakai.
        
    Returns:
        dict: {
            "profit_usdt": float,     # Estimasi profit jika TP tercapai
            "loss_usdt": float,       # Estimasi loss jika SL tercapai
            "profit_percent": float,  # ROI jika profit (terhadap margin)
            "loss_percent": float     # ROI jika loss (terhadap margin)
        }
    """
    if entry_price <= 0 or amount_usdt <= 0 or leverage <= 0:
        return {
            "profit_usdt": 0.0,
            "loss_usdt": 0.0,
            "profit_percent": 0.0,
            "loss_percent": 0.0
        }
    
    # Hitung position size dan quantity
    position_size_usdt = amount_usdt * leverage
    qty = position_size_usdt / entry_price
    
    # Hitung jarak ke TP dan SL
    if side.lower() == 'buy':
        # Long position: profit jika harga naik, loss jika turun
        profit_distance = tp_price - entry_price
        loss_distance = entry_price - sl_price
    else:
        # Short position: profit jika harga turun, loss jika naik
        profit_distance = entry_price - tp_price
        loss_distance = sl_price - entry_price
    
    # Hitung profit/loss dalam USDT
    profit_usdt = qty * abs(profit_distance)
    loss_usdt = qty * abs(loss_distance)
    
    # Hitung persentase ROI (terhadap margin, bukan position size)
    profit_percent = (profit_usdt / amount_usdt) * 100 if amount_usdt > 0 else 0
    loss_percent = (loss_usdt / amount_usdt) * 100 if amount_usdt > 0 else 0
    
    return {
        "profit_usdt": round(profit_usdt, 2),
        "loss_usdt": round(loss_usdt, 2),
        "profit_percent": round(profit_percent, 2),
        "loss_percent": round(loss_percent, 2)
    }

def calculate_trap_entry_setup(
    ai_sl_price: float,
    side: str,
    atr_value: float,
    atr_multiplier_tp: float,
    atr_multiplier_sl: float
) -> Dict[str, float]:
    """
    Hitung setup Trap Entry berdasarkan sl_price dari AI.
    Entry baru = AI sl_price (zona likuiditas)
    TP = entry ± ATR × atr_multiplier_tp
    SL = entry ∓ ATR × atr_multiplier_sl
    
    Args:
        ai_sl_price (float): Harga Stop Loss yang disarankan AI (akan jadi Entry).
        side (str): 'BUY' atau 'SELL'.
        atr_value (float): Nilai ATR saat ini.
        atr_multiplier_tp (float): Multiplier ATR untuk Take Profit.
        atr_multiplier_sl (float): Multiplier ATR untuk Stop Loss.
        
    Returns:
        dict: {
            'entry_price': float,
            'tp_price': float,
            'sl_price': float,
            'dist_tp': float,
            'dist_sl': float
        }
    """
    entry_price = ai_sl_price
    dist_tp = atr_value * atr_multiplier_tp
    dist_sl = atr_value * atr_multiplier_sl

    if side.upper() == 'BUY':
        # Long: TP di atas, SL di bawah
        tp_price = entry_price + dist_tp
        sl_price = entry_price - dist_sl
    else:  # SELL/SHORT
        # Short: TP di bawah, SL di atas
        tp_price = entry_price - dist_tp
        sl_price = entry_price + dist_sl

    return {
        'entry_price': entry_price,
        'tp_price': tp_price,
        'sl_price': sl_price,
        'dist_tp': dist_tp,
        'dist_sl': dist_sl
    }
