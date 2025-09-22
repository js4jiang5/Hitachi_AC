import esphome.codegen as cg
from esphome.components import climate_ir
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_TEMPERATURE, CONF_FAN_MODE

AUTO_LOAD = ["climate_ir"]

climate_ns = cg.esphome_ns.namespace("climate")
hitachi_ac344_ns = cg.esphome_ns.namespace("hitachi_ac344")
HitachiClimate = hitachi_ac344_ns.class_("HitachiClimate", climate_ir.ClimateIR)

CONF_HORIZONTAL_POSITION = "horizontal_position"
HORIZONTAL_DIRECTIONS = {
    "left_max": hitachi_ac344_ns.HITACHI_AC344_SWINGH_LEFT_MAX,
    "left": hitachi_ac344_ns.HITACHI_AC344_SWINGH_LEFT,
    "middle": hitachi_ac344_ns.HITACHI_AC344_SWINGH_MIDDLE,
    "right": hitachi_ac344_ns.HITACHI_AC344_SWINGH_RIGHT,
    "right_max": hitachi_ac344_ns.HITACHI_AC344_SWINGH_RIGHT_MAX,
}

HITACHI_SWING_MODES = {
    "horizontal": climate_ns.CLIMATE_SWING_HORIZONTAL,
    "vertical": climate_ns.CLIMATE_SWING_VERTICAL,
    "both": climate_ns.CLIMATE_SWING_BOTH,
    "off": climate_ns.CLIMATE_SWING_OFF,
}

HITACHI_FAN_MODES = {
    "auto": climate_ns.CLIMATE_FAN_AUTO,
    "low": climate_ns.CLIMATE_FAN_LOW,
    "medium": climate_ns.CLIMATE_FAN_MEDIUM,
    "high": climate_ns.CLIMATE_FAN_HIGH,
    "quiet": climate_ns.CLIMATE_FAN_QUIET,
}

CONF_SWING = "swing"
CONF_CUSTOM_COOL = "custom_cool"
CUSTOM_COOL_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_TEMPERATURE, default=28): cv.int_,
        cv.Optional(CONF_SWING, default="horizontal"): cv.enum(HITACHI_SWING_MODES),
        cv.Optional(CONF_FAN_MODE, default="auto"): cv.enum(HITACHI_FAN_MODES),
    }
)

CONF_CUSTOM_HEAT = "custom_heat"
CUSTOM_HEAT_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_TEMPERATURE, default=24): cv.int_,
        cv.Optional(CONF_SWING, default="off"): cv.enum(HITACHI_SWING_MODES),
        cv.Optional(CONF_FAN_MODE, default="auto"): cv.enum(HITACHI_FAN_MODES),
    }
)

CONF_CUSTOM_DRY = "custom_dry"
CUSTOM_DRY_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_TEMPERATURE, default=28): cv.int_,
        cv.Optional(CONF_SWING, default="horizontal"): cv.enum(HITACHI_SWING_MODES),
        cv.Optional(CONF_FAN_MODE, default="low"): cv.enum(HITACHI_FAN_MODES),
    }
)

CONF_CUSTOM_FAN_ONLY = "custom_fan_only"
CUSTOM_FAN_ONLY_SCHEMA = cv.Schema(
    {
        cv.Optional(CONF_SWING, default="off"): cv.enum(HITACHI_SWING_MODES),
        cv.Optional(CONF_FAN_MODE, default="low"): cv.enum(HITACHI_FAN_MODES),
    }
)

CONF_MILDEWPROOF = "mildewproof"

CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(HitachiClimate).extend(
    {
        cv.Optional(CONF_HORIZONTAL_POSITION, default="middle"): cv.enum(
            HORIZONTAL_DIRECTIONS
        ),
        cv.Optional(CONF_MILDEWPROOF, default=False): cv.boolean,
        cv.Optional(CONF_CUSTOM_COOL): CUSTOM_COOL_SCHEMA,
        cv.Optional(CONF_CUSTOM_HEAT): CUSTOM_HEAT_SCHEMA,
        cv.Optional(CONF_CUSTOM_DRY): CUSTOM_DRY_SCHEMA,
        cv.Optional(CONF_CUSTOM_FAN_ONLY): CUSTOM_FAN_ONLY_SCHEMA,
    }
)


async def to_code(config):
    var = await climate_ir.new_climate_ir(config)
    cg.add(var.set_horizontal_default(config[CONF_HORIZONTAL_POSITION]))
    cg.add(var.set_mildewproof(config[CONF_MILDEWPROOF]))

    if CONF_CUSTOM_COOL in config:
        cg.add(
            var.set_custom_cool(
                config[CONF_CUSTOM_COOL][CONF_TEMPERATURE],
                config[CONF_CUSTOM_COOL][CONF_SWING],
                config[CONF_CUSTOM_COOL][CONF_FAN_MODE],
            )
        )
    else:
        cg.add(
            var.set_custom_cool(
                28, climate_ns.CLIMATE_SWING_HORIZONTAL, climate_ns.CLIMATE_FAN_AUTO
            )
        )

    if CONF_CUSTOM_HEAT in config:
        cg.add(
            var.set_custom_heat(
                config[CONF_CUSTOM_HEAT][CONF_TEMPERATURE],
                config[CONF_CUSTOM_HEAT][CONF_SWING],
                config[CONF_CUSTOM_HEAT][CONF_FAN_MODE],
            )
        )
    else:
        cg.add(
            var.set_custom_heat(
                24, climate_ns.CLIMATE_SWING_OFF, climate_ns.CLIMATE_FAN_AUTO
            )
        )

    if CONF_CUSTOM_DRY in config:
        cg.add(
            var.set_custom_dry(
                config[CONF_CUSTOM_DRY][CONF_TEMPERATURE],
                config[CONF_CUSTOM_DRY][CONF_SWING],
                config[CONF_CUSTOM_DRY][CONF_FAN_MODE],
            )
        )
    else:
        cg.add(
            var.set_custom_dry(
                28, climate_ns.CLIMATE_SWING_HORIZONTAL, climate_ns.CLIMATE_FAN_LOW
            )
        )

    if CONF_CUSTOM_FAN_ONLY in config:
        cg.add(
            var.set_custom_fan_only(
                config[CONF_CUSTOM_FAN_ONLY][CONF_SWING],
                config[CONF_CUSTOM_FAN_ONLY][CONF_FAN_MODE],
            )
        )
    else:
        cg.add(
            var.set_custom_fan_only(
                climate_ns.CLIMATE_SWING_OFF, climate_ns.CLIMATE_FAN_LOW
            )
        )
