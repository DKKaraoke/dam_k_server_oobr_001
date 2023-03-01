import struct

from dam_k_server_oobr_001.customized_logger import getLogger

__RESERVE_SONG_WITH_OPTIONS_REQUEST_MESSAGE_ID = b"\x51\x10"
__RESERVE_SONG_WITH_OPTIONS_REQUEST_PAYLOAD_FIXED_PART = b"\x53\x50\x44\x45\x4e\x4d\x4f\x4b\x00\x00\x00\x00\x00\x00\x00\x00\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

__logger = getLogger("DamKServerOobr001")


def makePayload(option_count=0xFFFF):
    __logger.info(f"option_count={hex(option_count)}")
    options_length = 4 * option_count
    __logger.info(f"options_length={hex(options_length)}")

    message_payload: bytes = __RESERVE_SONG_WITH_OPTIONS_REQUEST_PAYLOAD_FIXED_PART
    message_payload += struct.pack(">H", option_count)

    payload: bytes = __RESERVE_SONG_WITH_OPTIONS_REQUEST_MESSAGE_ID
    payload += struct.pack(">H", len(message_payload))
    payload += message_payload
    __logger.info(f"payload={payload.hex()}")
    read_length = len(payload) + options_length
    __logger.info(f"read_length={hex(read_length)}")
    return payload
