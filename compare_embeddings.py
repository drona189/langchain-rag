from langchain_openai import OpenAIEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv

load_dotenv()

def main():
   # embedding_function = OpenAIEmbeddings()
   # vector = embedding_function.embed_query("apple")
   # print(f"Vector for 'apple': {vector}")
   # print(f"Vector length: {len(vector)}")

    evaluator = load_evaluator("pairwise_embedding_distance")
    words = ("apple", "iphone")
    x = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {x})")

if __name__ == "__main__":
    main()

