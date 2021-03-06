from bitmovin.resources import Resource


class MuxingInformationAudioTrack(Resource):

    def __init__(self, index, codec, codec_iso, bitrate, sampling_rate, channels):
        super().__init__()

        self.index = index
        self.codec = codec
        self.codec_iso = codec_iso
        self.bitrate = bitrate
        self.sampling_rate = sampling_rate
        self.channels = channels

    @classmethod
    def parse_from_json_object(cls, json_object):
        index = json_object.get('index')
        codec = json_object.get('codec')
        codec_iso = json_object.get('codecIso')
        bitrate = json_object.get('bitRate')
        sampling_rate = json_object.get('samplingRate')
        channels = json_object.get('channels')

        muxing_information_audio_track = MuxingInformationAudioTrack(
            index=index,
            codec=codec,
            codec_iso=codec_iso,
            bitrate=bitrate,
            sampling_rate=sampling_rate,
            channels=channels
        )
        return muxing_information_audio_track
