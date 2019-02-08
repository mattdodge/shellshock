# The import declares our reference and also makes our linters happy,
# shellshock won't actually import your file.
import customconverter
# The following would also work if you wanted to make the import actually
# work, in case you wanted to actually run your Python script too, not just
# the Shellshock output script
# from .coverters import customconverter


customconverter('test', 'things')
