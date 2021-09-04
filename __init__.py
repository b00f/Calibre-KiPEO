
from calibre.customize import EditBookToolPlugin
from calibre.customize import InterfaceActionBase
from calibre.ebooks.oeb.polish.container import get_container

class KiPEOPlugin(EditBookToolPlugin, InterfaceActionBase):
    name                = 'KiPEO' # Name of the plugin
    description         = 'Optimize Perssian/Arabic E-books for Amazon Kindle'
    supported_platforms = ['windows', 'osx', 'linux'] # Platforms this plugin will run on
    author              = 'Ali Bahraminezhad.' # The author of this plugin
    version             = (1, 0, 3)   # The version number of this plugin
    file_types          = set(['epub', 'awz3']) # The file types that this plugin will be applied to
    on_postprocess      = True # Run this plugin after conversion is complete
    minimum_calibre_version = (0, 7, 53)

