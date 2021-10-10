class DefendingPokemon():
    def __init__(self, card_data=object, health=0, energies=[], isAsleep=False, isBurned=False, isConfused=False, isParalyzed=False, isPoisoned=False, isProtectedFromAttackNextTurn=False):
        self.card_data = card_data
        self.health = health
        self.energies = energies
        self.isAsleep = isAsleep
        self.isBurned = isBurned
        self.isConfused = isConfused
        self.isParalyzed = isParalyzed
        self.isPoisoned = isPoisoned
        self.isProtectedFromAttackNextTurn = isProtectedFromAttackNextTurn