import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 2
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

#for n in range(10):
 #   blockchain.mine(Block("Block " + str(n+1)))

#while blockchain.head != None:
   # print(blockchain.head)
#    blockchain.head = blockchain.head.next




from hashlib import sha256
MAX_NONCE=50000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
def mine(block_number,transactions,previous_hash,prefiz_zeros):
    prefix_str='0'*prefiz_zeros
    for nonce in range(MAX_NONCE):
        print(f'mining {nonce}')
        text = str(block_number)+transactions+previous_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f'bitcoin mined with nonce : {nonce}')
            return new_hash
    raise BaseException(f"couldn't find correct hash after trying {MAX_NONCE} times")
if __name__=='__main__':
    transactions='''
    John->Jeb->20,
    Mando->John->45
    '''
    import time
    start = time.time()
    print('starting...')
    new_hash = mine(666627,transactions,'00000000000000000006a293574d0f999c0b653535720741778d5c24f76a3921',dificulty)
    print(f'finished mining\ntime: {time.time()-start} seconds')
    print(new_hash)