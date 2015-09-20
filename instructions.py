from dicts import *

def create_add(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100000
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_addi(string):
	parts = string.split()
	opcode = 0b00100000000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_addiu(string):
	parts = string.split()
	opcode = 0b00100100000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode

def create_addu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100001
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_and(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100100
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_andi(string):
	parts = string.split()
	opcode = 0b00110000000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_beq(string):
	parts = string.split()
	opcode = 0b00010000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	offset = parts[3]
	if not rt in registers.keys() or not rt in registers.keys() or not offset in labels.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= offset_num
	return opcode


def create_beql(string):
	parts = string.split()
	opcode = 0b01010000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	offset = parts[3]
	if not rt in registers.keys() or not rt in registers.keys() or not offset in labels.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= offset_num
	return opcode


def create_bgez(string):
	parts = string.split()
	opcode = 0b00000100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode

def create_bgezal(string):
	parts = string.split()
	opcode = 0b00000100000100010000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bgezall(string):
	parts = string.split()
	opcode = 0b00000100000100110000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bgezl(string):
	parts = string.split()
	opcode = 0b00000100000001110000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bgtz(string):
	parts = string.split()
	opcode = 0b00011100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bgtzl(string):
	parts = string.split()
	opcode = 0b01011100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_blez(string):
	parts = string.split()
	opcode = 0b00011000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_blezl(string):
	parts = string.split()
	opcode = 0b01011000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bltz(string):
	parts = string.split()
	opcode = 0b00000100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bltzal(string):
	parts = string.split()
	opcode = 0b00000100000100000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bltzall(string):
	parts = string.split()
	opcode = 0b00000100000100100000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bltzl(string):
	parts = string.split()
	opcode = 0b00000100000000100000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	offset = parts[2]
	if not rs in registers.keys() or not offset in labels: 
		error(string)
	rs_num = registers[rs]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= offset
	return opcode


def create_bne(string):
	parts = string.split()
	opcode = 0b00010100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	offset = parts[3]
	if not rt in registers.keys() or not rt in registers.keys() or not offset in labels.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= offset_num
	return opcode


def create_bnel(string):
	parts = string.split()
	opcode = 0b01010100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	offset = parts[3]
	if not rt in registers.keys() or not rt in registers.keys() or not offset in labels.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	offset_num = labels[offset]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= offset_num
	return opcode


def create_break(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001101
	return opcode


def create_cop0(string):
	parts = string.split()
	opcode = 0b01000000000000000000000000000000
	return opcode


def create_cop1(string):
	parts = string.split()
	opcode = 0b01000100000000000000000000000000
	return opcode


def create_cop2(string):
	parts = string.split()
	opcode = 0b01001000000000000000000000000000
	return opcode


def create_cop3(string):
	parts = string.split()
	opcode = 0b01001100000000000000000000000000
	return opcode


def create_dadd(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000101100
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode

def create_daddi(string):
	parts = string.split()
	opcode = 0b01100000000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_daddiu(string):
	parts = string.split()
	opcode = 0b01100100000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_daddu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000101101
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_ddiv(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011110
	if len(parts) < 4:
		error(string)
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_ddivu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011111
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_div(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011010
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_divu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011011
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_dmult(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011100
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_dmultu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011101
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_dsll(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000111000
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_dsll32(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000111100
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_dsllv(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010100
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_dsra(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000111011
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_dsra32(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010111
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode

def create_dsrav(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010111
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode

def create_dsrl(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000111010
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_dsrl32(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000111110
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_dsrlv(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010110
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_dsub(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000101110
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_dsubu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000101111
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_j(string):
	parts = string.split()
	opcode = 0b00001000000000000000000000000000
	if len(parts) < 2:
		error(string)
	addr = parts[1]
	if not addr in labels.keys():
		error(string)
	addr_num = labels[addr]
	opcode |= addr_num
	return opcode


def create_jal(string):
	parts = string.split()
	opcode = 0b00001100000000000000000000000000
	if len(parts) < 2:
		error(string)
	addr = parts[1]
	if not addr in labels.keys():
		error(string)
	addr_num = labels[addr]
	opcode |= addr_num
	return opcode


def create_jalr(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001001
	if len(parts) < 2:
		error(string)
	rs = parts[1].replace(',', '')
	if(len(parts) >= 3):
		rd = parts[2]
		if not rd in labels.keys():
			error(string)
		rd_num = registers[rd]
	else:
		rd_num = 31
	if not rs in registers.keys():
		error(string)
	rs_num = registers[addr]
	opcode |= (rs_num << 21)
	opcode |= (rd_num << 11)
	return opcode


def create_jr(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001000
	if len(parts) < 2:
		error(string)
	rs = parts[1].replace(',', '')
	if not rs in registers.keys():
		error(string)
	rs_num = registers[addr]
	opcode |= (rs_num << 21)
	return opcode


def create_lb(string):
	parts = string.split()
	opcode = 0b10000000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lbu(string):
	parts = string.split()
	opcode = 0b10010000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_ld(string):
	parts = string.split()
	opcode = 0b11011100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_ldc1(string):
	parts = string.split()
	opcode = 0b11010100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_ldc2(string):
	parts = string.split()
	opcode = 0b11011000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_ldl(string):
	parts = string.split()
	opcode = 0b01101000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_ldr(string):
	parts = string.split()
	opcode = 0b01101100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lh(string):
	parts = string.split()
	opcode = 0b10000100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lhu(string):
	parts = string.split()
	opcode = 0b10010100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_ll(string):
	parts = string.split()
	opcode = 0b11000000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lld(string):
	parts = string.split()
	opcode = 0b11010000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lui(string):
	parts = string.split()
	opcode = 0b00111100000000000000000000000000
	if len(parts) < 2:
		error(string)
	rt = parts[1].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_lw(string):
	parts = string.split()
	opcode = 0b10001100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lwc1(string):
	parts = string.split()
	opcode = 0b11000100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lwc2(string):
	parts = string.split()
	opcode = 0b11001000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lwc3(string):
	parts = string.split()
	opcode = 0b11001100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lwl(string):
	parts = string.split()
	opcode = 0b10001000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lwr(string):
	parts = string.split()
	opcode = 0b10011000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_lwu(string):
	parts = string.split()
	opcode = 0b10011100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_mfhi(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010000
	if len(parts) < 2:
		error(string)
	rd = parts[1]
	if not rd in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rd_num << 11)
	return opcode


def create_mflo(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010010
	if len(parts) < 2:
		error(string)
	rd = parts[1]
	if not rd in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rd_num << 11)
	return opcode


def create_movn(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001011
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_movz(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001010
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_mthi(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010001
	if len(parts) < 2:
		error(string)
	rt = parts[1]
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rt_num << 21)
	return opcode


def create_mtlo(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000010011
	if len(parts) < 2:
		error(string)
	rt = parts[1]
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rt_num << 21)
	return opcode


def create_mult(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_multu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000011001
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_nor(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100111
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_or(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100101
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_ori(string):
	parts = string.split()
	opcode = 0b00110100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_pref(string):
	parts = string.split()
	opcode = 0b11001100000000000000000000000000
	error(string)


def create_sb(string):
	parts = string.split()
	opcode = 0b10100000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sc(string):
	parts = string.split()
	opcode = 0b11100000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_scd(string):
	parts = string.split()
	opcode = 0b11110000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sd(string):
	parts = string.split()
	opcode = 0b11111100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sdc1(string):
	parts = string.split()
	opcode = 0b11110100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sdc2(string):
	parts = string.split()
	opcode = 0b11111000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sdl(string):
	parts = string.split()
	opcode = 0b10110000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sdr(string):
	parts = string.split()
	opcode = 0b10110100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sh(string):
	parts = string.split()
	opcode = 0b10100100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sll(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000000000
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_sllv(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000000100
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_slt(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000101010
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_slti(string):
	parts = string.split()
	opcode = 0b00101000000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_sltiu(string):
	parts = string.split()
	opcode = 0b00101100000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


def create_sltu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000101011
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_sra(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000000011
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_srav(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000000111
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_srl(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000000010
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rt = parts[2].replace(',', '')
	sa = parts[3]
	if not rs in registers.keys() or not rt in registers.keys() or not sa in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	sa_num = registers[sa]
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	opcode |= (sa_num << 6)
	return opcode


def create_srlv(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000000110
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_sub(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100010
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_subu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100011
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_sw(string):
	parts = string.split()
	opcode = 0b10101100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_swc1(string):
	parts = string.split()
	opcode = 0b11100100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_swc2(string):
	parts = string.split()
	opcode = 0b11101000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_swc3(string):
	parts = string.split()
	opcode = 0b11101100000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_swl(string):
	parts = string.split()
	opcode = 0b10101000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_swr(string):
	parts = string.split()
	opcode = 0b10111000000000000000000000000000
	if len(parts) < 3:
		error(string)
	rt = parts[1].replace(',', '')
	total_offset = parts[2]
	offset_parts = offset.split('(')
	if len(offset_parts) < 2:
		error(string)
	offset = int(offset_parts[0])
	offset = offset + offset_parts[1].replace(')', '')
	if not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	opcode |= (rt_num << 16)
	opcode |= offset
	return opcode


def create_sync(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001111
	return opcode


def create_syscall(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000001100
	if len(parts) < 2:
		error(string)
	code = int(parts[1])
	opcode |= (code << 6)
	return opcode


def create_teq(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000110100
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_teqi(string):
	parts = string.split()
	opcode = 0b00000100000011000000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	imm = int(parts[2])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= imm
	return opcode


def create_tge(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000110000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_tgei(string):
	parts = string.split()
	opcode = 0b00000100000010000000000000000000
	if len(parts) < 4:
		error(string)
	rs = parts[1].replace(',', '')
	imm = int(parts[2])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= imm
	return opcode


def create_tgeiu(string):
	parts = string.split()
	opcode = 0b00000100000010010000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	imm = int(parts[2])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= imm
	return opcode


def create_tgeu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000110001
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_tlt(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000110010
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_tlti(string):
	parts = string.split()
	opcode = 0b00000100000010100000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	imm = int(parts[2])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= imm
	return opcode


def create_tltiu(string):
	parts = string.split()
	opcode = 0b00000100000010110000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	imm = int(parts[2])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= imm
	return opcode


def create_tltu(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000110011
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_tne(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000110110
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	rt = parts[2]
	if not rs in registers.keys() or not rt in registers.keys():
		error(string)
	rs_num = registers[rs]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	return opcode


def create_tnei(string):
	parts = string.split()
	opcode = 0b00000100000011100000000000000000
	if len(parts) < 3:
		error(string)
	rs = parts[1].replace(',', '')
	imm = int(parts[2])
	if not rt in registers.keys():
		error(string)
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= imm
	return opcode


def create_xor(string):
	parts = string.split()
	opcode = 0b00000000000000000000000000100110
	if len(parts) < 4:
		error(string)
	rd = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	rt = parts[3]
	if not rd in registers.keys() or not rt in registers.keys() or not rs in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	rs_num = registers[rs]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= (rd_num << 11)
	return opcode


def create_xori(string):
	parts = string.split()
	opcode = 0b00111000000000000000000000000000
	if len(parts) < 4:
		error(string)
	rt = parts[1].replace(',', '')
	rs = parts[2].replace(',', '')
	imm = int(parts[3])
	if not rt in registers.keys() or not rt in registers.keys():
		error(string)
	rd_num = registers[rd]
	rt_num = registers[rt]
	opcode |= (rs_num << 21)
	opcode |= (rt_num << 16)
	opcode |= imm
	return opcode


