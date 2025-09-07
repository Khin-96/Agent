from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json

load_dotenv()
logging.basicConfig(level=logging.INFO)

user_name = "Kinga"
mem0 = MemoryClient()


def add_memory(messages):
    """
    Add a list of messages to memory for the given user.
    Each message should be a dict: {"role": "user"|"assistant", "content": "text"}
    """
    mem0.add(messages, user_id=user_name)
    logging.info("Memory added successfully.")


def get_memory_by_query(query=None):
    """
    Retrieve memories matching a query for the given user.
    If no query is provided, a default query about preferences is used.
    """
    if query is None:
        query = f"What are {user_name}'s preferences?"
    
    results = mem0.search(query, user_id=user_name)
    
    memories = [
        {
            "memory": result["memory"],
            "updated_at": result["updated_at"]
        }
        for result in results
    ]
    
    memories_str = json.dumps(memories, indent=2)
    print(f"Memories: {memories_str}")
    return memories_str


if __name__ == "__main__":
    # Example: Add a memory
    messages_to_add = [
        {"role": "user", "content": "I really like Nairobi National Park."},
        {"role": "assistant", "content": "That is a good choice."},
        {"role": "user", "content": "I think so too."},
        {"role": "assistant", "content": "What is your favorite song by them?"}
    ]
    add_memory(messages_to_add)

    # Example: Retrieve memories
    get_memory_by_query()

    # Example: Custom query
    # get_memory_by_query("Tell me what Kinga enjoys doing in Nairobi.")
