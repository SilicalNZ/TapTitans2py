from tap_titans.utils.base import Struct, field

from tap_titans.models.player import Artifacts, Card, ClanScrolls, HeroWeapons, Pets


class PlayerArtifact(Struct):
    artifact_id: Artifacts
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
    scroll_id: ClanScrolls = field(name="ScrollId")


class PlayerHeroWeapon(Struct):
    level: int = field(name="Level")
    hero_id: HeroWeapons = field(name="HelperID")


class PlayerPet(Struct):
    level: int
    pet_id: Pets


class PlayerSeasonalArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerSkill(Struct):
    level: int
    skill_id: str


class PlayerData(Struct):
    additive_relic_multiplier: int
    artifacts: tuple[PlayerArtifact, ...]
    badge_count: PlayerBadgeCount
    cards: tuple[PlayerCard, ...]
    challenge_tournaments_participation: int
    challenge_tournaments_undisputed_count: int
    clan_code: str
    clan_name: str
    clan_scroll: tuple[PlayerClanScroll, ...]
    country_code: str
    crafting_shards_spent: int
    current_card_currency: int
    current_world_id: int
    daily_raid_tickets: int
    equipment_set: tuple[str, ...]
    equipment_set_count: int
    hero_weapon: tuple[PlayerHeroWeapon, ...]
    loyalty_level: int
    max_stage: int
    name: str
    pets: tuple[PlayerPet, ...]
    player_code: str
    player_raid_level: int
    previous_rank: str
    raid_wildcard_count: int
    relics_received: str
    relics_spent: str
    role: str
    seasonal_artifacts: tuple[PlayerSeasonalArtifact, ...]
    seasonal_relic_multiplier: int
    seasonal_relics_received: str
    seasonal_relics_spent: str
    skill_tree: tuple[PlayerSkill, ...]
    titan_points: int
    total_card_level: int
    total_clan_scrolls: int
    total_hero_weapons: int = field(name="total_helper_weapons")
    total_pet_levels: int
    total_raid_player_xp: int
    total_skill_points: int
    total_tournaments: int
    undisputed_count: int
    weekly_ticket_count: int
