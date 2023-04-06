#!/bin/python3

# 3-1 Names
names = ['alice', 'bob', 'charlie', 'dave', 'eve', 'grace', 'mallory']

print(names[0].title())
print(names[1].title())
print(names[-1].title())

# 3-2 Greetings
#ind = 0
#for i in names :
#        print('Greetings ' +names[ind].title())
#        ind = ind+1
# better loop:
for name in names :
        print(f"Greetings {name.title()}")

# 3-4 Guest list
guests = ['einstein', 'feynman', 'bohr']
#ind = 0
#for i in guests :
#        print(f"Dear Mr/Mrs {guests[ind].title()}, please attend dinner with me.")
#        ind = ind+1
#better loop:
for guest in guests :
        print(f"Dear Mr/Mrs {guest.title()}, please attend dinner with me.")

# 3-5 Change list
rsvpno = 'feynman'
print(f"{rsvpno.title()} can't make it.")
guests.remove(rsvpno)
guests.append('tyson')
#ind = 0
#for i in guests :
#        print(f"Dear Mr/Mrs {guests[ind].title()}, please attend dinner with me.")
#        ind = ind+1
#better loop:
for guest in guests :
        print(f"Dear Mr/Mrs {guest.title()}, please attend dinner with me.")

# 3-6 Add to list
print(f"We have found a bigger table!")
guests.insert(0, 'hill')
guests.insert(3, 'sagan')
guests.append('pascal')
#ind = 0
#for i in guests :
#        print(f"Dear Mr/Mrs {guests[ind].title()}, please attend dinner with me.")
#        ind = ind+1
#better loop:
for guest in guests :
        print(f"Dear Mr/Mrs {guest.title()}, please attend dinner with me.")

# 3-7 Shrink list
print(f"Well, damn. That table is gone, now we only have 2 seats")
count = len(guests) -1
while count > 1 :
        print(f"Dear Mr/Mrs {guests[count].title()}, I'm sorry but we no longer have a seat for you.")
        guests.pop(count)
        count -= 1

#ind = 0
#for i in guests :
#        print(f"Dear Mr/Mrs {guests[ind].title()}, we still have a seat for you.")
#        ind = ind+1
#better loop:
for guest in guests :
        print(f"Dear Mr/Mrs {guest.title()}, we still have a seat for you.")

del guests[1]
del guests[0]

print(guests)