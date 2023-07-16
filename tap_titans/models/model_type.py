from enum import Enum


class Event(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnect"
    ERROR = "error"
    CONNECTION_ERROR = "connect_error"
    CLAN_REMOVED = "unsub_clan"
    RAID_ATTACK = "attack"
    RAID_START = "start"
    CLAN_ADDED_RAID_START = "sub_start"
    RAID_END = "end"
    RAID_RETIRE = "retire"
    RAID_CYCLE_RESET = "cycle_reset"
    CLAN_ADDED_CYCLE = "sub_cycle"
    RAID_TARGET_CHANGED = "target"


class TitanPart(str, Enum):
    ArmorLegRight = "ArmorLegUpperRight"
    ArmorHandLeft = "ArmorHandLeft"
    ArmorHandRight = "ArmorHandRight"
    ArmorLegLeft = "ArmorLegUpperLeft"
    ArmorChest = "ArmorChestUpper"
    ArmorArmRight = "ArmorArmUpperRight"
    ArmorArmLeft = "ArmorArmUpperLeft"
    ArmorHead = "ArmorHead"
    BodyLegRight = "BodyLegUpperRight"
    BodyHandLeft = "BodyHandLeft"
    BodyHandRight = "BodyHandRight"
    BodyLegLeft = "BodyLegUpperLeft"
    BodyChest = "BodyChestUpper"
    BodyArmRight = "BodyArmUpperRight"
    BodyArmLeft = "BodyArmUpperLeft"
    BodyHead = "BodyHead"
    SkeletonLegRight = "SkeletonLegUpperRight"
    SkeletonHandLeft = "SkeletonHandLeft"
    SkeletonHandRight = "SkeletonHandRight"
    SkeletonLegLeft = "SkeletonLegUpperLeft"
    SkeletonChest = "SkeletonChestUpper"
    SkeletonArmRight = "SkeletonArmUpperRight"
    SkeletonArmLeft = "SkeletonArmUpperLeft"
    SkeletonHead = "SkeletonHead"


class CardBonus(str, Enum):
    TeamTacticsClanMoraleBoost = "TeamTacticsClanMoraleBoost"
    MirrorForceBoost = "MirrorForceBoost"


class Card(str, Enum):
    MoonBeam = "MoonBeam"
    Fragmentize = "Fragmentize"
    SkullBash = "SkullBash"
    RazorWind = "RazorWind"
    WhipOfLightning = "WhipOfLightning"
    ClanshipBarrage = "BurstCount"
    PurifyingBlast = "Purify"
    PsychicShackles = "LimbBurst"
    FlakShot = "FlakShot"
    CosmicHaymaker = "Haymaker"
    ChainOfVengeance = "ChainLightning"
    MirrorForce = "MirrorForce"
    CelestialStatic = "CelestialStatic"
    BurningInferno = "BurningAttack"
    AcidDrench = "PoisonAttack"
    DecayingAttack = "DecayingAttack"
    FusionBomb = "Fuse"
    GrimShadow = "Shadow"
    ThrivingPlague = "PlagueAttack"
    Radioactivity = "Disease"
    RavenousSwarm = "Swarm"
    RuinousRain = "RuinousRust"
    CorrosiveBubbles = "PowerBubble"
    Maelstrom = "RuneAttack"
    CrushingInstinct = "ExecutionersAxe"
    InsanityVoid = "CrushingVoid"
    RancidGas = "MentalFocus"
    InspiringForce = "ImpactAttack"
    SoulFire = "InnerTruth"
    VictoryMarch = "FinisherAttack"
    PrismaticRift = "SuperheatMetal"
    AncestralFavor = "BurstBoost"
    GraspingVines = "LimbSupport"
    TotemOfPower = "TotemFairySkill"
    TeamTactics = "TeamTactics"
    SkeletalSmash = "SpinalTap"
    AstralEcho = "AstralEcho"

    # Placeholder for api changes
    UNKNOWN = "UNKNOWN"

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class Enemy(str, Enum):
    Enemy1 = "Enemy1"
    Enemy2 = "Enemy2"
    Enemy3 = "Enemy3"
    Enemy4 = "Enemy4"
    Enemy5 = "Enemy5"
    Enemy6 = "Enemy6"
    Enemy7 = "Enemy7"
    Enemy8 = "Enemy8"


class EnemyName(str, Enum):
    Lojak = "Lojak"
    Takedar = "Takedar"
    Jukk = "Jukk"
    Sterl = "Sterl"
    Mohaca = "Mohaca"
    Terro = "Terro"
    Klonk = "Klonk"
    Priker = "Priker"


class TargetState(Enum):
    NoTarget = 0
    Crossed = 1
    Checked = 2


class TargetStateStr(str, Enum):
    NoTarget = "0"
    Crossed = "1"
    Checked = "2"


class TargetStatePart(str, Enum):
    Head = "Head"
    Chest = "ChestUpper"
    ArmRight = "ArmUpperRight"
    ArmLeft = "ArmUpperLeft"
    LegRight = "LegUpperRight"
    LegLeft = "LegUpperLeft"
    HandRight = "HandRight"
    HandLeft = "HandLeft"


class TitanRaidBonus(str, Enum):
    RaidAttackDuration = "RaidAttackDuration"
    AfflictedDamage = "AfflictedDamage"
    AfflictedDuration = "AfflictedDuration"
    LimbDamage = "LimbDamage"
    AllRaidDamage = "AllRaidDamage"
    SupportEffect = "SupportEffect"
    AfflictedChance = "AfflictedChance"
    ChestDamage = "ChestDamage"
    HeadDamage = "HeadDamage"
    BodyDamage = "BodyDamage"
    ArmorDamage = "ArmorDamage"
    BurstDamage = "BurstDamage"
    BurstChance = "BurstChance"
