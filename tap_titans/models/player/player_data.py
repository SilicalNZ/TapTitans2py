from tap_titans.utils.base import Struct, field

from tap_titans.models.player import Artifacts, Card, ClanScrolls, HeroWeapons, Pets


class PlayerArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerBadgeCount(Struct):
    zero: int = field(name="0")
    one: int = field(name="1")
    two: int = field(name="2")
    three: int = field(name="3")
    four: int = field(name="4")


class PlayerCard(Struct):
    level: int
    quantity_received: int
    quantity_spent: int
    skill_name: Card


class PlayerClanScroll(Struct):
    level: int = field(name="Level")
    scroll_id: str = field(name="ScrollId")


class PlayerHeroWeapon(Struct):
    level: int = field(name="Level")
    hero_id: str = field(name="HelperID")


class PlayerPet(Struct):
    level: int
    pet_id: str


class PlayerSeasonalArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerSkill(Struct):
    level: int
    skill_id: str


class PlayerTitanCard(Struct):
    titan_id: str
    level: int
    quantity_received: int
    quantity_spent: int


class PlayerRaidResearchTree(Struct):
    armor_damage: float | None = field(name="ArmorDamage", default=None)
    body_damage: float | None = field(name="BodyDamage", default=None)
    chest_damage: float | None = field(name="ChestDamage", default=None)
    head_damage: float | None = field(name="HeadDamage", default=None)
    limb_damage: float | None = field(name="LimbDamage", default=None)
    raid_enemy_1_damage: float | None = field(name="RaidEnemy1Damage", default=None)
    raid_enemy_2_damage: float | None = field(name="RaidEnemy2Damage", default=None)
    raid_enemy_3_damage: float | None = field(name="RaidEnemy3Damage", default=None)
    raid_enemy_4_damage: float | None = field(name="RaidEnemy4Damage", default=None)
    raid_enemy_5_damage: float | None = field(name="RaidEnemy5Damage", default=None)
    raid_enemy_6_damage: float | None = field(name="RaidEnemy6Damage", default=None)
    raid_enemy_7_damage: float | None = field(name="RaidEnemy7Damage", default=None)
    raid_enemy_8_damage: float | None = field(name="RaidEnemy8Damage", default=None)


class PlayerData(Struct):
    player_code: str | None
    country_code: str | None
    max_stage: int | None
    crafting_shards_spent: int | None
    raid_wildcard_count: int | None
    current_card_currency: int | None
    additive_relic_multiplier: int | None
    relics_received: str | None
    relics_spent: str | None
    summon_level: int | None
    name: str | None
    total_tournaments: int | None
    undisputed_count: int | None
    titan_points: str | None
    total_raid_player_xp: int | None
    player_raid_level: int | None
    total_card_level: int | None
    equipment_set_count: int | None
    total_pet_levels: int | None
    total_skill_points: int | None
    total_clan_scrolls: int | None
    challenge_tournaments_participation: int | None
    challenge_tournaments_undisputed_count: int | None
    current_world_id: int | None
    clan_code: str | None
    clan_name: str | None
    role: str | None
    weekly_ticket_count: int | None
    titan_cards: tuple[PlayerTitanCard, ...] | None
    raid_research_tree : PlayerRaidResearchTree | None
    loyalty_level: int | None
    daily_raid_tickets: int | None
    previous_rank: str | None
    artifacts: tuple[PlayerArtifact, ...] | None
    seasonal_relics_received: str | None
    seasonal_relics_spent: str | None
    seasonal_relic_multiplier: int | None
    seasonal_artifacts: tuple[PlayerSeasonalArtifact, ...] | None
    cards: tuple[PlayerCard, ...] | None
    pets: tuple[PlayerPet, ...] | None
    badge_count: PlayerBadgeCount | None
    hero_weapon: tuple[PlayerHeroWeapon, ...] | None
    clan_scroll: tuple[PlayerClanScroll, ...] | None
    skill_tree: tuple[PlayerSkill, ...] | None
    equipment_set: tuple[str, ...] | None
    # field() is a kwarg and must be defined last
    total_hero_weapons: int | None = field(name="total_helper_weapons", default=None)
