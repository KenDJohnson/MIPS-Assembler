from dicts import *
from ctypes import *
import sys

global labels
global linecount
global byte_offset

def error_hander(  ):
	print("[-] Error  on line %d:" % linecount)


def add_data(asm_data):
	label = ""
	datatype = ""
	size = 0
	values = []
	for letter in asm_data:
		if letter != ':':
			label += letter
		else:
			break
	asm_data = asm_data.strip(label+":")
	asm_data = asm_data.lstrip()
	print(label)
	for letter in asm_data:
		if letter != ' ':
			datatype += letter
		else:
			break
	asm_data = asm_data.strip(datatype)
	asm_data = asm_data.lstrip()
	print(datatype)
	if datatype != ".asciiz" and datatype != ".ascii" and datatype != ".space":
		if datatype == ".byte":
			data = []
			for val in asm_data.split(','):
				data.append(int(val))
			return (bytes(data), label)
		elif datatype == ".halfword":
			data = []
			for val in asm_data.split(','):
				if int(val) <= 0xff :
					data.append(0)
				data.append(int(val))
			return (bytes(data), label)
		elif datatype == ".word":
			data = []
			for val in asm_data.split(','):
				if int(val) <=  0xffffff:
					data.append(0)
				if int(val) <= 0xffff:
					data.append(0)
				if int(val) <= 0xff:
					data.append(0)
				data.append(int(val))
			return (bytes(data), label)
		values = asm_data.split(',')
	elif datatype == ".ascii":
		chunks = asm_data.split("\"")
		if len(chunks) < 3:
			error()
		return (bytes(chunks[1]), label)
	elif datatype == ".asciiz":
		chunks = asm_data.split("\"")
		if len(chunks) < 3:
			error()
		return (ytes(chunks[1]+"\x00"), label)
	elif datatype == ".space":
		return (bytes(int(asm_data.rstrip())), label)
		
	

def main():
	if len(sys.argv) < 3:
		printf("usage: assemler.py <input> <output>")
		sys.exit(-1)
	
	byte_offset = 0
	in_text = False
	in_data = True
	in_file = open(sys.argv[1], 'r')
	linecount = 0
	data_bytes = bytes()
	for line in in_file.readlines():
		linecount += 1
		line_parts = line.split("#")
		if len(line_parts) < 1:
			continue
		if len(line_parts[0]) < 1:
			continue
		if line.__contains__(".data"):
			in_data = True
			in_text = False
			continue
		if line.__contains__(".text"):
			in_data = False
			in_text = True
			continue
		asm = line_parts[0]
		if in_data:
			ret, label = add_data(asm)
			if ret is None:
				continue
			labels.update({label, byte_offset})
			byte_offset += len(ret)
			data_bytes += ret 
			
		
	out_file = open(sys.argv[2], 'wb')
	out_file.write(data_bytes)
	out_file.close()
	in_file.close()
if __name__ == "__main__":
	main()
