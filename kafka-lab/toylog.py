import sys, os
LOG = "events.log"

def produce(msg):
    with open(LOG, "a") as f:
        f.write(msg + "\n")

def consume(group):
    
    pos_file = f"{group}.offset"
    pos = int(open(pos_file).read()) if os.path.exists(pos_file) else 0
    
    with open(LOG) as f:
        lines = f.read().splitlines()
    
    for i, line in enumerate(lines[pos:], start=pos):
        print(f"[{group}] offset={i} {line}")
    
    open(pos_file, "w").write(str(len(lines)))

if __name__ == "__main__":
    cmd, arg = sys.argv[1], sys.argv[2]
    produce(arg) if cmd == "produce" else consume(arg)