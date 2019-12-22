from population import population
population_size=100
mutation=0.01
target_word=input("Enter Target Word: ")
entities=population(population_size,target_word)
entities.evolution()
