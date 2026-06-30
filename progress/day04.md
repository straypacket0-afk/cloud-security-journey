## Day 04 - OverTheWire Bandit (S2)

**Date:** June 30, 2026  
**Journey Day:** Day 04

### What I Studied
- OverTheWire Bandit Levels 6-10

### Challenges Faced
- Bandit 6: Finding a specific 33-byte file owned by bandit7:bandit6 using `find`
- Bandit 8: Finding the only unique line in a large file
- Bandit 9: Extracting human-readable strings
- Bandit 10: Base64 decoding

### How I Solved Them
- **Bandit 6**: `find / -user bandit7 -group bandit6 -size 33c`
- **Bandit 7**: `grep "millionth" data.txt`
- **Bandit 8**: `sort data.txt | uniq -u`
- **Bandit 9**: `strings data.txt | grep "==="`
- **Bandit 10**: `base64 -d data.txt`

### New Concepts
- Advanced `find` command usage
- `strings`, `uniq -u`, Base64 encoding/decoding

### Progress
Cleared Bandit 6-10

**Tomorrow's Plan:** Networking + IPv6 + more Base64 practice

---
*Hyped and locked in.*
