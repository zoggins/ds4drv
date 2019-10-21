from ..action import ReportAction

ReportAction.add_option("--dump-reports", action="store_true",
                        help="Prints controller input reports")


class ReportActionDump(ReportAction):
    """Pretty prints the reports to the log."""

    def __init__(self, *args, **kwargs):
        super(ReportActionDump, self).__init__(*args, **kwargs)
        self.timer = self.create_timer(0.02, self.dump)

    def enable(self):
        self.timer.start()

    def disable(self):
        self.timer.stop()

    def load_options(self, options):
        if options.dump_reports:
            self.enable()
        else:
            self.disable()

    def dump(self, report):
#        dump = "Report dump\n"
#        for key in report.__slots__:
#            value = getattr(report, key)
#            dump += "    {0}: {1}\n".format(key, value)
#
#        self.logger.info(dump)
#
#        return True

         dump = "{0}".format(str(bin(getattr(report, "dpad_up")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "dpad_down")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "dpad_left")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "dpad_right")))[2:])

         dump += "{0}".format(str(bin(getattr(report, "button_cross")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_circle")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_square")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_triangle")))[2:])

         dump += "{0}".format(str(bin(getattr(report, "button_l1")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_l2")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_l3")))[2:])

         dump += "{0}".format(str(bin(getattr(report, "button_r1")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_r2")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_r3")))[2:])

         dump += "{0}".format(str(bin(getattr(report, "button_share")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_options")))[2:])
	 dump += "{0}".format(str(bin(getattr(report, "button_ps")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "button_trackpad")))[2:])

         dump += "{0}".format(str(bin(getattr(report,"left_analog_x")))[2:].zfill(8)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"left_analog_y")))[2:].zfill(8)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"right_analog_x")))[2:].zfill(8)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"right_analog_y")))[2:].zfill(8)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"l2_analog")))[2:].zfill(8)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"r2_analog")))[2:].zfill(8)[::-1])
         
         dump += "{0}".format(str(bin(getattr(report, "trackpad_touch0_active")))[2:])
         dump += "{0}".format(str(bin(getattr(report, "trackpad_touch1_active")))[2:])

         dump += "{0}".format(str(bin(getattr(report,"trackpad_touch0_x")))[2:].zfill(16)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"trackpad_touch0_y")))[2:].zfill(16)[::-1])

         dump += "{0}".format(str(bin(getattr(report,"trackpad_touch1_x")))[2:].zfill(16)[::-1])
         dump += "{0}".format(str(bin(getattr(report,"trackpad_touch1_y")))[2:].zfill(16)[::-1])

         self.logger.info(dump)
         return True
