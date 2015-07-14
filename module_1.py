import sys, csv, operator


#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f = open('suc_ph.csv', 'r')
  suc = {}
  for index, line in enumerate (f):
    row=line.split(',')
    if row[0] in suc:
      suc[row[0]] +=1
    else:
      suc[row[0]] = 1

      f.close
  suc_list = sorted(suc.items(), key=operator.itemgetter(1), reverse = True)
  print "1. The region with the most SUC is " + suc_list[0][0]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  if school_year == '2010-2011':
      num=2
  elif school_year == '2011-2012':
      num=3
  elif school_year == '2012-2013':
      num=4

  f = open('suc_ph.csv', 'r')
  enrollees = {}
  for index, line in enumerate (f): 
    row=line.split(',')
    if row[0] in enrollees: 
      if row[num].isdigit(): 
        enrollees[row[0]] += int(row[num])  
    else:
      if row[num].isdigit():
        enrollees[row[0]] = int(row[num])

      f.close
  enrollees_list = sorted(enrollees.items(), key=operator.itemgetter(1), reverse = True)
  print "3. The region with the most SUC Enrollees is " + enrollees_list[0][0]


#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  if school_year == '2009-2010':
      num=5
  elif school_year == '2010-2011':
      num=6
  elif school_year == '2011-2012':
      num=7
  

  f = open('suc_ph.csv', 'r')
  graduates = {}
  for index, line in enumerate (f):
    row=line.split(',')
    if row[0] in graduates:
      if row[num].isdigit():
        graduates[row[0]] += int(row[num])
    else:
      if row[num].isdigit():
        graduates[row[0]] = int(row[num])

      f.close
  graduates_list = sorted(graduates.items(), key=operator.itemgetter(1), reverse = True)
  print "3. The region with the most SUC graduates is " + graduates_list[0][0]

  #print "3. The region with the most SUC graduates is Cagayan Valley (R-II)"

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  if level == 'BS' and school_year == '2010-2011': 
    num=2
  elif level == 'BS' and school_year == '2011-2012': 
    num=5
  elif level == 'BS' and school_year == '2012-2013': 
    num=8
  elif level == 'MS' and school_year == '2010-2011': 
    num=3
  elif level == 'MS' and school_year == '2011-2012':
    num=6
  elif level == 'MS' and school_year == '2012-2013': 
    num=9
  elif level == 'PhD' and school_year == '2010-2011': 
    num=4
  elif level == 'PhD' and school_year == '2011-2012': 
    num=7
  elif level == 'PhD' and school_year == '2012-2013': 
    num=10

  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  cheapestsuc = {}
  for index, line in enumerate (f):
    row=line.split(',')
    if row[1] not in cheapestsuc:
      if row[num].isdigit():
        cheapestsuc[row[1]] = int(row[num])

      f.close
  cheapestsuc_list = sorted(cheapestsuc.items(), key=operator.itemgetter(1), reverse = False)

  print "4. Top 3 cheapest SUC for " + level + " in school year " + school_year
  print "  1. " + cheapestsuc_list[0][0]
  print "  2. " + cheapestsuc_list[1][0]
  print "  3. " + cheapestsuc_list[2][0]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  if level == 'BS' and school_year == '2010-2011': 
    num=2
  elif level == 'BS' and school_year == '2011-2012': 
    num=5
  elif level == 'BS' and school_year == '2012-2013': 
    num=8
  elif level == 'MS' and school_year == '2010-2011': 
    num=3
  elif level == 'MS' and school_year == '2011-2012':
    num=6
  elif level == 'MS' and school_year == '2012-2013': 
    num=9
  elif level == 'PhD' and school_year == '2010-2011': 
    num=4
  elif level == 'PhD' and school_year == '2011-2012': 
    num=7
  elif level == 'PhD' and school_year == '2012-2013': 
    num=10

  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  expensivesuc = {}
  for index, line in enumerate (f):
    row=line.split(',')
    if row[1] not in   expensivesuc:
      if row[num].isdigit():
          expensivesuc[row[1]] = int(row[num])

      f.close
    expensivesuc_list = sorted(  expensivesuc.items(), key=operator.itemgetter(1), reverse = True)

  print "5. Top 3 expensive SUC for " + level + " in school year " +  school_year 
  print "  1. " +  expensivesuc_list[0][0]
  print "  2. " +  expensivesuc_list[1][0]
  print "  3. " +  expensivesuc_list[2][0]


#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  increasesuc = {}
  x=0
  for index, line in enumerate (f):
      row=line.split (',')
      if row[1] not in increasesuc:
        if (row[2].isdigit() and row[8].isdigit()):
          if ((row[8]) > (row[2])):
            increasesuc[row[1]] = row[1]
            x+=1
            print "  " , x , increasesuc[row[1]]
            
          f.close
    
  

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  
  f = open('performancesucprclicensureexam20102012.csv', 'r')
  # row[3] Passers ng 2010
  # row[7] Takers ng 2010
  # row[2] discipline
  if school_year == '2010':
      passed=3
      take=7
  elif school_year == '2011':
      passed=4
      take=8
  elif school_year == '2012':
      passed=5
      take=9
  
  topdiscipline = {}
  for index, line in enumerate (f):
    row=line.split(',')
    if row[2] not in topdiscipline:
      passers=0
      takers=0
      if row[passed].isdigit() and row[take].isdigit():
        passers += float (row[passed])
        takers += float (row [take])
        passingrate = (passers/takers) * 100
        topdiscipline[row[2]] = passingrate

      f.close
      


  topdiscipline_list = sorted(topdiscipline.items(), key=operator.itemgetter(1), reverse = True)

  print "7. The discipline which has the highest passing rate is " + topdiscipline_list[0][0]   
      


#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  f = open('performancesucprclicensureexam20102012.csv', 'r')
  topAccountancy = {}
  x=0
  for index, line in enumerate (f):
    row=line.split(',')
    if row[2]  == 'Accountancy':
      if row[4].isdigit() and row[8].isdigit():
          passer= float (row[4])
          taker = float (row[8])
          passingrate= (passer/taker) *100
          topAccountancy[row[1]] =  passingrate
      

      f.close
  topAccountancy_list = sorted(topAccountancy.items(), key=operator.itemgetter(1), reverse = True)

  print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2011"
  print "  1. " + topAccountancy_list[0][0]
  print "  2. " + topAccountancy_list[1][0]
  print "  3. " + topAccountancy_list[2][0]



def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()