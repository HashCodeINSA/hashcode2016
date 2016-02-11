
#
#   DM = DroneManager
#   OM = OrderManager
#   WM = WarehouseManager
#

# tant qu'on a pas atteint la fin de la simulation
while not DM.simu_end(): 
    # tant qu'on a un drone disponible
    while not (d = DM.next_available_drone()) is None: 
        # si une commande non traitée subsiste
        if not (o = OM.next_unhandled_order()) is None: 
            # tant que le drone n'est pas plein ou que la commande n'est pas complète
            while not d.is_full(o.item_left()) or not o.item_left() is None: 
                # si on a au moins une une warehouse qui possède l'item
                if not (w = WM.get_closest_having(o.item_left())) is None: 
                    # on demande au drone de charger
                    d.load(w, o.item_left(), o)
                else: # aucune warehouse ne contient cet item 
                    # on abandonne la commande doit être abandonnée
                    o.cancel()
            # quand on arrive là, la commande est abandonnée OU la commande est chargée OU le drone est plein
            # si le drone est plein OU la commande est complètement chargée
            if d.is_full(o.item_left()) or o.item_left() is None:
                # on dit au drone de faire la livraison
                d.deliver(o)
        else: # si aucune commande existe 
            # le drone attend
            d.wait()
    #
    # on fait avancer la simulation d'un pas
    #
    DM.next_turn() 
