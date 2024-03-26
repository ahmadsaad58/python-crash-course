from dataclasses import dataclass
from datetime import datetime
import csv


@dataclass
class Leetcode():
	number: int
	name: str
	date: datetime
	level: str
	description: str

	def __post_init__(self) -> None: 
		self.number = int(self.number)
		self.date = datetime.strptime(self.date, '%m-%d-%Y')
		

class LeetcodeCounter():
	def __init__(self) -> None:
		self.questions = []
		self.easy = 0
		self.medium = 0
		self.hard = 0

	def append(self, question: Leetcode) -> None:
		match question.level.lower():
			case 'easy':
				self.easy += 1
			case 'medium':
				self.medium += 1
			case 'hard':
				self.hard += 1
		self.questions.append(question)

	def pop(self) -> Leetcode:
		return self.questions.pop()

	def __len__(self) -> int:
		return len(self.questions)
	
	def __str__(self) -> str:
		return "\n".join([f'{question.name}: {question.level}' for question in self.questions])
	
	def get_questions_by_date(self, my_date: datetime) -> list[Leetcode]:
		return [question for question in self.questions if question.date == my_date]
	
	def get_questions_by_level(self, my_level: str) -> list[Leetcode]:
		return [question for question in self.questions if question.level.lower() == my_level.lower()]
			
	

def main():
	counter = LeetcodeCounter()
	
	with open("doordash_leetcode.csv", 'r', newline='\n') as my_file: 
		questions_reader = csv.reader(my_file, delimiter=',')
		for line in questions_reader:
			counter.append(Leetcode(*[item.strip() for item in line]))

	print(f'Total Completed: {len(counter)}')
	print(f'Total hard: {counter.hard} \nTotal Medium: {counter.medium}')
	
	# print('\nQuestions from Today:')
	# questions_from_today = counter.get_questions_by_date(datetime.strptime('03-08-24', '%m-%d-%y'))
	# print('\n'.join([f'{question.name}: {question.level}' for question in questions_from_today]))
	
	# print('\nMedium Questions:')
	# medium_questions = counter.get_questions_by_level('Medium')
	# print('\n'.join([f'{question.name}' for question in medium_questions]))

	# print('\nHard Questions:')
	# hard_questions = counter.get_questions_by_level('Hard')
	# print('\n'.join([f'{question.name}' for question in hard_questions]))


if __name__ == '__main__': 
	main()
