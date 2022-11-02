
import hashlib

# data = "Udit Kundu"
# result = hashlib.sha256(data.encode())
# print(result.hexdigest())


# Generate hexadecimal number
def hash_generator(data):
    return hashlib.sha256(data.encode()).hexdigest()


class Block:
    def __init__(self, data, prev_hash, block_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.block_hash = block_hash

    # Format the block in a dictonary format
    def format_in_dict(self):
        return {
            "data": self.data,
            "prev_hash": self.prev_hash,
            "block_hash": self.block_hash
        }


class BlockChain:
    def __init__(self):
        genesis_block_data = "gen-block"
        prev_hash = "0000000000"
        block_hash = hash_generator(genesis_block_data)

        # Creating the genesis block in the time of creation of block chain
        genesis_block = Block(genesis_block_data, prev_hash, block_hash)

        # And sotre it on a list in a formated mannner
        self.blocks = [genesis_block.format_in_dict()]

    def add_block(self, data):
        # Taking prev hash from the last block of block chain
        prev_hash = self.blocks[- 1]["block_hash"]
        block_hash = hash_generator(data + prev_hash)

        # Creating new block and apped it on the list of blocks
        new_block = Block(data, prev_hash, block_hash)
        self.blocks.append(new_block.format_in_dict())

    def show_all_blocks(self):
        # Show all blocks in the formatted manner
        for block in self.blocks:
            print(block)


bc = BlockChain()
# print(bc.blocks[0].data)
bc.add_block("our 2nd block")
bc.add_block("our 3rd block")
# print(bc.blocks[0].block_hash)
# print(bc.blocks[1].prev_hash)
print(bc.blocks)
bc.show_all_blocks()
