from stenogotchi.ui.hw.waveshare4 import WaveshareV4

def display_for(config):
    # config has been normalized already in utils.load_config
    if config['ui']['display']['type'] == 'waveshare_4':
        return WaveshareV4(config)
    else:
        print("no display specified")