import sys
from git import Repo

class Profiler:
	def __init__(self, repo_path):
		self.repo = Repo(repo_path)
		self.user_emails = set()
		self.user_emails.add(self.getUserEmail())

	def getUserEmail(self):
		reader = self.repo.config_reader()
		val = reader.get_value("user", "email")
		return val

	def addUserEmails(self, emails):
		for email in emails:
			self.user_emails.add(email)

	def getCommitsList(self, number_of_commits):
		commits_list = list(self.repo.iter_commits('master', max_count=number_of_commits))
		print("Total number of commits:", len(commits_list))
		commits_list = [c for c in commits_list if c.author.email in self.user_emails]
		print("Number of your commits:", len(commits_list))
		return commits_list

	def retrieveDiffs(self, commits_list):
		for commit in commits_list:
			# print("\t", commit.message)
			print(commit.stats.files)

	def getProfile(self):
		commits_list = self.getCommitsList(number_of_commits=None)
		self.retrieveDiffs(commits_list)