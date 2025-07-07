from enum import Enum
from typing import NewType


class ClanEvents(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnect"
    ERROR = "error"
    CONNECTION_ERROR = "connect_error"
    CLAN_REMOVED = "unsub_clan"
    RAID_ATTACK_START = "start_attack"
    RAID_ATTACK_END = "attack"
    RAID_START = "start"
    CLAN_ADDED_RAID_START = "sub_start"
    RAID_END = "end"
    RAID_RETIRE = "retire"
    RAID_CYCLE_RESET = "cycle_reset"
    CLAN_ADDED_CYCLE = "sub_cycle"
    RAID_TARGET_CHANGED = "target"
    CLAN_JOIN = "join"
    CLAN_LEAVE = "leave"
    CLAN_KICK = "kick"
    PLAYER_MORALE = "morale"
    CLAN_SYNC = "sync"


class PlayerEvents(str, Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnect"
    ERROR = "error"
    CONNECTION_ERROR = "connect_error"


class TitanParts(str, Enum):
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


class CardBonuses(str, Enum):
    TeamTacticsClanMoraleBoost = "TeamTacticsClanMoraleBoost"
    MirrorForceBoost = "MirrorForceBoost"


class Cards(str, Enum):
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
    BlazingInferno = "BurningAttack"
    AcidDrench = "PoisonAttack"
    DecayingStrike = "DecayingAttack"
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
    Amplify = "MagicPotion"
    RadiantKaleidoscope = "TriangleSupport"
    SandsOfTime = "SandsOfTime"
    GuardBreak = "Weaken"
    ElectroZap = "CosmicBarb"


class EnemyIDs(str, Enum):
    Enemy1 = "Enemy1"
    Enemy2 = "Enemy2"
    Enemy3 = "Enemy3"
    Enemy4 = "Enemy4"
    Enemy5 = "Enemy5"
    Enemy6 = "Enemy6"
    Enemy7 = "Enemy7"
    Enemy8 = "Enemy8"


class EnemyNames(str, Enum):
    Lojak = "Lojak"
    Takedar = "Takedar"
    Jukk = "Jukk"
    Sterl = "Sterl"
    Mohaca = "Mohaca"
    Terro = "Terro"
    Klonk = "Klonk"
    Priker = "Priker"


class TargetStates(str, Enum):
    NoTarget = "0"
    Crossed = "1"
    Checked = "2"
    Yellow = "3"


class TargetStateParts(str, Enum):
    Head = "Head"
    Chest = "ChestUpper"
    ArmRight = "ArmUpperRight"
    ArmLeft = "ArmUpperLeft"
    LegRight = "LegUpperRight"
    LegLeft = "LegUpperLeft"
    HandRight = "HandRight"
    HandLeft = "HandLeft"


class TitanRaidBonuses(str, Enum):
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


class TitanCurseTypes(str, Enum):
    Burst = "BurstDamagePerCurse"
    Body = "BodyDamagePerCurse"
    Affliction = "AfflictedDamagePerCurse"


class TitanAreaTypes(str, Enum):
    AllArmsHPMult = "AllArmsHPMult"
    ArmorArmsHPMult = "ArmorArmsHPMult"
    ArmorLegsHPMult = "ArmorLegsHPMult"
    AllHeadHPMult = "AllHeadHPMult"
    AllArmorHPMult = "AllArmorHPMult"
    AllLimbsHPMult = "AllLimbsHPMult"
    AllTorsoHPMult = "AllTorsoHPMult"
    AllLegsHPMult = "AllLegsHPMult"
