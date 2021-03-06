class XmlErrorEnum(object):
    ERROR_101 = "Network attribute 'code' cannot be null"
    ERROR_102 = "Network attribute 'code' must consist of a two-character string"
    ERROR_103 = "Network element 'startDate' is required"
    ERROR_105 = "Network element 'startDate' must occur before Network element 'endDate' if 'endDate' is available"
    ERROR_105b = "Network element 'startDate' must occur before earliest Station element 'startDate'"
    ERROR_105c = "Network element 'endDate' (if available) must occur after latest Station 'endDate'"
    ERROR_152 = "Station epochs cannot overlap in time"
    # Station level validation
    ERROR_201 = "Station attribute 'code' cannot be null"
    ERROR_202 = "Station code too long empty string or wrong characters"
    ERROR_203 = "Station startDate required"
    ERROR_205 = "Station startDate < endDate when endDate is available"
    ERROR_206 = "Station latitude invalid"
    ERROR_207 = "Station longitude invalid"
    ERROR_209 = "Station creation time must exist"
    ERROR_210 = "Station elevation must be equal to or above Channel elevation"
    ERROR_251 = "Distance from station to channel must not exceed 1 km"
    ERROR_252 = "Channel epoch overlap not allowed"
    # Channel level validation
    ERROR_301 = "Channel attribute 'code' cannot be null must match [A-Za-z0-9\*\?]{13}"
    ERROR_302 = "Channel attribute 'location' cannot be null must match ([A-Za-z0-9\*\?\-\ ]{12})?"
    ERROR_303 = "Channel startDate is required"
    ERROR_305 = "Channel startDate < endDate when endDate available"
    ERROR_306 = "Channel latitude is invalid"
    ERROR_307 = "Channel longitude is invalid"
    ERROR_308 = "Channel depth is required"
    ERROR_309 = "Channel azimuth is invalid"
    ERROR_310 = "If Channel sample rate = 0 no Response should be included"
    ERROR_311 = "Channel sensor description cannot be null/empty"
    ERROR_312 = "Calibration unit is invalid"
    ERROR_314 = "Invalid Dip value"
    ERROR_315 = "Invalid channel orientation"
    # Response level validation
    ERROR_401 = "The 'number' attribute of Response::Stage element must start at 1 and be sequential"
    ERROR_402 = "The element of a stage must match the element of the preceding stage except for stages 0 or 1."
    ERROR_403 = "The element StageGain::Value or InstrumentSensitivity::Value must be non-zero."
    ERROR_405 = "If Channel sample rate = 0 no Response should be included."
    ERROR_406 = "If Channel sample rate > 0 at least one stage must be included and be comprised of units gain and sample rate."
    ERROR_407 = "If Channel sample rate > 0 total instrument response must exist as either or ."
    ERROR_408 = "The value of Channel::SampleRate must be equal to the value of Decimation::InputSampleRate divided by Decimation::Factor of the final response stage."
    ERROR_409 = "Response stages having Coefficient FIR ResponseList or a PolesZeros with with transfer function type Digital must include a Decimation element."
    ERROR_410 = "Any FIR instrument type must include coefficient elements."
    ERROR_411 = "InputUnits for Stage-Sensitivity must come from approved list of unit names."
    ERROR_412 = "OutputUnits for Stage-Sensitivity must come from approved list of unit names."
    ERROR_413 = "If the value of Stage::Decimation::Factor is > 1 then Stage::Decimation::Correction must be non-zero."
    ERROR_511 = "Input Units for Stage::Filter must come from approved list of unit names."
    ERROR_512 = "OutputUnits for Stage::Filter must come from approved list of unit names."
