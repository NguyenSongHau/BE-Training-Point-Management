from base.serializers import BaseSerializer
from schools.models import Criterion, Semester, Class, Faculty


class FacultySerializer(BaseSerializer):
	class Meta:
		model = Faculty
		fields = ["id", "name", "educational_system"]

	def to_representation(self, faculty):
		data = super().to_representation(faculty)

		if "educational_system" in self.fields and faculty.educational_system:
			data["educational_system"] = f"{faculty.educational_system}"

		return data


class ClassSerializer(BaseSerializer):
	class Meta:
		model = Class
		fields = ["id", "name", "major", "academic_year"]

	def to_representation(self, sclass):
		data = super().to_representation(sclass)

		if "major" in self.fields and sclass.major:
			data["major"] = f"{sclass.major}"
		if "academic_year" in self.fields and sclass.academic_year:
			data["academic_year"] = f"{sclass.academic_year}"

		return data


class SemesterSerializer(BaseSerializer):
	class Meta:
		model = Semester
		fields = ["id", "original_name", "code", "academic_year", "start_date", "end_date"]

	def to_representation(self, semester):
		data = super().to_representation(semester)

		if "academic_year" in self.fields and semester.academic_year:
			data["academic_year"] = f"{semester.academic_year}"

		return data


class CriterionSerializer(BaseSerializer):
	class Meta:
		model = Criterion
		fields = ["id", "name", "max_point", "description"]
