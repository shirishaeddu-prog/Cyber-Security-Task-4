# Firewall Rule Simulation

rules = []

def add_rule(port, action):
    rules.append({"port": port, "action": action})
    print("Rule added:", action, "port", port)

def test_port(port):
    for rule in rules:
        if rule["port"] == port:
            print("Port", port, "->", rule["action"])
            return
    print("Port", port, "-> ALLOWED")

def show_rules():
    print("\nCurrent Firewall Rules:")
    if not rules:
        print("No rules")
    for r in rules:
        print("Port:", r["port"], "| Action:", r["action"])

# Block Telnet port 23
add_rule(23, "BLOCK")
show_rules()

# Test blocked port
print("\nTesting:")
test_port(23)
test_port(80)

# Allow SSH port 22
add_rule(22, "ALLOW")
show_rules()

# Test SSH
test_port(22)