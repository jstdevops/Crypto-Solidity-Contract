from brownie import JSTToken, accounts, network

def main():
    # Connect to a local network or specify 'mainnet', 'rinkeby', etc.
    network.connect('development')
    
    # Use a pre-funded account or create a new one
    deployer = accounts[0]
    
    # Deploy the contract
    initial_supply = 1000000 * (10 ** 18)
    token = JSTToken.deploy(initial_supply, {'from': deployer})
    
    print(f"JST Token deployed to: {token.address}")
    
    # Mint new tokens (onlyOwner function call)
    mint_amount = 1000 * (10 ** 18)
    token.mint(deployer, mint_amount, {'from': deployer})
    print(f"Minted {mint_amount} JST to {deployer}")
    
    # Burn tokens
    burn_amount = 500 * (10 ** 18)
    token.burn(burn_amount, {'from': deployer})
    print(f"Burned {burn_amount} JST from {deployer}")

if __name__ == "__main__":
    main()
