import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir
from esphome.const import CONF_ID

AUTO_LOAD = ["climate_ir"]

hitachi_ac_ns = cg.esphome_ns.namespace("hitachi_ac")
HitachiClimate = hitachi_ac_ns.class_("HitachiClimate", climate_ir.ClimateIR)

CONF_HORIZONTAL_DEFAULT = "horizontal_default"
HORIZONTAL_DIRECTIONS = {
    "left_max": hitachi_ac_ns.HITACHI_AC_SWINGH_LEFT_MAX,
    "left": hitachi_ac_ns.HITACHI_AC_SWINGH_LEFT,
    "middle": hitachi_ac_ns.HITACHI_AC_SWINGH_MIDDLE,
    "right": hitachi_ac_ns.HITACHI_AC_SWINGH_RIGHT,
    "right_max": hitachi_ac_ns.HITACHI_AC_SWINGH_RIGHT_MAX,
}

CONFIG_SCHEMA = climate_ir.CLIMATE_IR_WITH_RECEIVER_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(HitachiClimate),
        cv.Optional(CONF_HORIZONTAL_DEFAULT, default="middle"): cv.enum(
            HORIZONTAL_DIRECTIONS
        ),
    }
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await climate_ir.register_climate_ir(var, config)
    cg.add(var.set_horizontal_default(config[CONF_HORIZONTAL_DEFAULT]))
