import gdb

X86_ALL_REGS = ['gs', 'fs', 'es', 'ds', 'edi', 'esi', 'ebx', 'edx', 'ecx', 'eax', 'ebp', 'eip', 'cs', 'efl', 'esp', 'ss', 'dr0', 'dr1', 'dr2', 'dr3', 'dr6', 'dr7', 'di', 'si', 'bx', 'dx', 'cx', 'ax', 'bp', 'ip', 'fl', 'sp', 'bl', 'dl', 'cl', 'al', 'bh', 'dh', 'ch', 'ah', 'fpcw', 'fpsw', 'fptw', 'fopcode', 'fpip', 'fpipsel', 'fpdp', 'fpdpsel', 'st0', 'st1', 'st2', 'st3', 'st4', 'st5', 'st6', 'st7', 'mm0', 'mm1','mm2', 'mm3', 'mm4', 'mm5', 'mm6', 'mm7', 'mxcsr', 'xmm0', 'xmm1', 'xmm2', 'xmm3', 'xmm4', 'xmm5', 'xmm6', 'xmm7', 'iopl', 'of', 'df', 'if', 'tf', 'sf', 'zf', 'af', 'pf', 'cf', 'vip', 'vif', 'xmm0l', 'xmm1l', 'xmm2l', 'xmm3l', 'xmm4l', 'xmm5l', 'xmm6l', 'xmm7l', 'xmm0h', 'xmm1h', 'xmm2h', 'xmm3h', 'xmm4h', 'xmm5h', 'xmm6h', 'xmm7h', 'xmm0/0', 'xmm0/1', 'xmm0/2', 'xmm0/3', 'xmm1/0', 'xmm1/1', 'xmm1/2', 'xmm1/3', 'xmm2/0', 'xmm2/1', 'xmm2/2', 'xmm2/3', 'xmm3/0', 'xmm3/1', 'xmm3/2', 'xmm3/3', 'xmm4/0', 'xmm4/1', 'xmm4/2', 'xmm4/3', 'xmm5/0', 'xmm5/1', 'xmm5/2', 'xmm5/3', 'xmm6/0', 'xmm6/1', 'xmm6/2', 'xmm6/3', 'xmm7/0', 'xmm7/1', 'xmm7/2', 'xmm7/3']
X86_BASIC_REGS = ['eax', 'ebx', 'ecx', 'edx', 'esi', 'edi', 'esp', 'ebp', 'eip']
AMD64_ALL_REGS = ['rax', 'rcx', 'rdx', 'rbx', 'rsp', 'rbp', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'rip', 'efl', 'cs', 'ds', 'es', 'fs', 'gs', 'ss', 'dr0', 'dr1', 'dr2', 'dr3', 'dr6', 'dr7', 'fpcw', 'fpsw', 'fptw', 'st0', 'st1','st2', 'st3', 'st4', 'st5', 'st6', 'st7', 'mm0', 'mm1', 'mm2', 'mm3', 'mm4', 'mm5', 'mm6', 'mm7', 'mxcsr', 'xmm0', 'xmm1', 'xmm2', 'xmm3', 'xmm4', 'xmm5', 'xmm6', 'xmm7', 'xmm8', 'xmm9', 'xmm10', 'xmm11', 'xmm12', 'xmm13', 'xmm14', 'xmm15', 'xmm0/0', 'xmm0/1', 'xmm0/2', 'xmm0/3', 'xmm1/0', 'xmm1/1', 'xmm1/2', 'xmm1/3', 'xmm2/0', 'xmm2/1', 'xmm2/2', 'xmm2/3', 'xmm3/0', 'xmm3/1', 'xmm3/2', 'xmm3/3', 'xmm4/0', 'xmm4/1', 'xmm4/2', 'xmm4/3', 'xmm5/0', 'xmm5/1', 'xmm5/2', 'xmm5/3', 'xmm6/0', 'xmm6/1', 'xmm6/2', 'xmm6/3', 'xmm7/0', 'xmm7/1', 'xmm7/2', 'xmm7/3', 'xmm8/0', 'xmm8/1', 'xmm8/2', 'xmm8/3', 'xmm9/0', 'xmm9/1', 'xmm9/2', 'xmm9/3', 'xmm10/0', 'xmm10/1', 'xmm10/2', 'xmm10/3', 'xmm11/0', 'xmm11/1', 'xmm11/2', 'xmm11/3', 'xmm12/0', 'xmm12/1', 'xmm12/2', 'xmm12/3', 'xmm13/0', 'xmm13/1', 'xmm13/2', 'xmm13/3', 'xmm14/0', 'xmm14/1', 'xmm14/2', 'xmm14/3', 'xmm15/0', 'xmm15/1', 'xmm15/2', 'xmm15/3', 'xmm0l', 'xmm1l', 'xmm2l', 'xmm3l', 'xmm4l', 'xmm5l','xmm6l', 'xmm7l', 'xmm8l', 'xmm9l', 'xmm10l', 'xmm11l', 'xmm12l', 'xmm13l', 'xmm14l', 'xmm15l', 'xmm0h', 'xmm1h', 'xmm2h', 'xmm3h', 'xmm4h', 'xmm5h', 'xmm6h', 'xmm7h', 'xmm8h', 'xmm9h', 'xmm10h', 'xmm11h', 'xmm12h', 'xmm13h', 'xmm14h', 'xmm15h', 'exfrom', 'exto', 'eax', 'ecx', 'edx', 'ebx', 'esp', 'ebp', 'esi', 'edi','r8d', 'r9d', 'r10d', 'r11d', 'r12d', 'r13d', 'r14d', 'r15d', 'eip', 'ax', 'cx','dx', 'bx', 'sp', 'bp', 'si', 'di', 'r8w', 'r9w', 'r10w', 'r11w', 'r12w', 'r13w', 'r14w', 'r15w', 'ip', 'fl', 'al', 'cl', 'dl', 'bl', 'spl', 'bpl', 'sil', 'dil', 'r8b', 'r9b', 'r10b', 'r11b', 'r12b', 'r13b', 'r14b', 'r15b', 'ah', 'ch', 'dh', 'bh', 'iopl', 'of', 'df', 'if', 'tf', 'sf', 'zf', 'af', 'pf', 'cf', 'vip', 'vif']
AMD64_BASIC_REGS = ['rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi', 'rsp', 'rbp', 'rip', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']

class GDBStateExporter(gdb.Command):
	"""
		Usage:
	"""
	def __init__(self):
		gdb.Command.__init__(self, 'angr', gdb.COMMAND_STACK)
		self.p_long = gdb.lookup_type('long').pointer()
		self.is_x86 = self.p_long.sizeof == 4

	def _get_register(self, reg):
        """
        Get current register value
        """

        expr = '$' + reg

        try:
            val = self._normalize_long(long(gdb.parse_and_eval(expr)))
        except:
            return None
        return val

    def _normalize_long(self, l):
        return (0xffffffff if self.is_x86 else 0xffffffffffffffff) & l


    def invoke(self, arg, from_tty):
        """
        The core of the command
        """
        print "running"

GDBStateExporter()