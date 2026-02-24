from datetime import datetime as dt

def empty_litter_tray() -> dict:
   """
   Simulate emptying the cat's litter tray.

   Returns:
   response (dict): A dictionary with a single key 'action_taken' descrining the time the litter tray was emptied.
   """
   current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
   return {"action_taken": f"Litter tray emptied at {current_time}."}


def order_catnip(quantity_grams: int) -> dict:
   """
   Simulate ordering catnip for a cat.

   Parameters:
   quantity_grams (int): The amount of catnip to order in grams.

   Returns:
   response (dict): A dictionary with a single key 'action_taken' describing the quantity of catnip ordered and the time of order.
   """
   current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
   return {"action_taken": f"Ordered {quantity_grams} grams of catnip at {current_time}."}