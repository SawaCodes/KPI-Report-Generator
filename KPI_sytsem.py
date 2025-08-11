
import time
import tkinter as tk
from tkinter import messagebox

def end_timer_fn(start_time):
    return time.time() - start_time

def start_timer():
    return time.time()
def main():
    dissemination_total_time = 0
    final_report_total_time = 0
    evaluation_of_report_total_time = 0
    Confirm = True
    while Confirm:
        file_received = input("Press 'Y' to indicate file received or 'q' to quit: ").strip().lower()
        if file_received == 'y':
            total_cycle_time = start_timer()
            print("Process started.")
            project_started = input("Has the project started? Press 'Y' for yes or 'q' to quit: ").strip().lower()
            if project_started == 'y':
                Disemmination = 1000
                Final_report = 2000
                Evaluation_of_report = 3000
                continue_process = True
                cost = 0
                total_parts = 0
                parts_automated = 0
                Error = 0
                while continue_process:
                    project_part_selection = input("Select the project process (planning, conducting, reporting): ").strip().lower()
                    if project_part_selection == 'reporting':
                        reporting_part = input("Select the reporting process (dissemination, final report, evaluation of report): ").strip().lower()
                        if reporting_part == 'dissemination':
                            dissemination_total_time = start_timer()
                            cost += Disemmination
                            total_parts += 1
                            print("Starting dissemination process...")
                            Automate_1 = input("Automate the dissemination process? (Y/N): ").strip().lower()
                            if Automate_1 == 'y':
                                print("Automating dissemination process...")
                                print("Work simulated for dissemination automation.")
                                time.sleep(2)
                                print("Dissemination process automated successfully.")
                                parts_automated += 1
                                Ammend_1= input ("Do you want to ammend the automated dissemination information? (Y/N): ").strip().lower()
                                if Ammend_1 == 'y':
                                    time.sleep(2)
                                    print("Automating dissemination process...")
                                    Error += 1
                                    dissemination_total_time = end_timer_fn(dissemination_total_time)
                                else:
                                    time.sleep(2)
                                    print("No amendments made to the automated dissemination information.")
                                    dissemination_total_time = end_timer_fn(dissemination_total_time)
                            else:
                                input("Please fill in the dissemination information manually and type Enter when done.")
                                dissemination_total_time = end_timer_fn(dissemination_total_time)
                        elif reporting_part == 'final report':
                            cost += Final_report
                            total_parts += 1
                            final_report_total_time = start_timer()
                            print("Starting final report process...")
                            Automate_2 = input("Automate the final report process? (Y/N): ").strip().lower()
                            if Automate_2 == 'y':
                                print("Automating final report process...")
                                print("Work simulated for final report automation.")
                                time.sleep(2)
                                print("Final report process automated successfully.")
                                parts_automated += 1
                                Ammend_2= input ("Do you want to ammend the automated final report information? (Y/N): ").strip().lower()
                                if Ammend_2 == 'y':
                                    time.sleep(2)
                                    print("Automating final report process...")
                                    Error += 1
                                    final_report_total_time = end_timer_fn(final_report_total_time)
                                else:
                                    time.sleep(2)
                                    print("No amendments made to the automated final report information.")
                                    final_report_total_time = end_timer_fn(final_report_total_time)
                            else:
                                input("Please fill in the final report information manually and type Enter when done.")
                                final_report_total_time = end_timer_fn(final_report_total_time)
                        elif reporting_part == 'evaluation of report':
                            evaluation_of_report_total_time = start_timer()
                            cost += Evaluation_of_report
                            total_parts += 1
                            print("Starting evaluation of report process...")
                            Automate_3 = input("Automate the evaluation of report process? (Y/N): ").strip().lower()
                            if Automate_3 == 'y':
                                print("Automating evaluation of report process...")
                                print("Work simulated for evaluation of report automation.")
                                time.sleep(2)
                                print("Evaluation of report process automated successfully.")
                                parts_automated += 1
                                Ammend_3= input ("Do you want to ammend the automated evaluation of report information? (Y/N): ").strip().lower()
                                if Ammend_3 == 'y':
                                    time.sleep(2)
                                    print("Automating evaluation of report process...")
                                    Error += 1
                                    evaluation_of_report_total_time = end_timer_fn(evaluation_of_report_total_time)
                                else:
                                    time.sleep(2)
                                    print("No amendments made to the automated evaluation of report information.")
                                    evaluation_of_report_total_time = end_timer_fn(evaluation_of_report_total_time)
                            else:
                                input("Please fill in the information for the evaluation of report manually and type Enter when done.")
                                evaluation_of_report_total_time = end_timer_fn(evaluation_of_report_total_time)
                        else:
                            print("Invalid reporting part selected.")
                    else:
                        print("Invalid project process selected. Please choose again.")
                    Continue = input("Do you want to continue the work cycle time? (Y/N): ").strip().lower()
                    if Continue == 'y':
                        continue_process = True
                    else:
                        continue_process = False
                        reporting_total_time = dissemination_total_time + final_report_total_time + evaluation_of_report_total_time
                        print(f"Total time for dissemination: {dissemination_total_time:.2f} seconds")
                        print(f"Total time for final report: {final_report_total_time:.2f} seconds")
                        print(f"Total time for evaluation of report: {evaluation_of_report_total_time:.2f} seconds")
                        print(f"Total time for reporting: {reporting_total_time:.2f} seconds")
                print(f"Total cost of the process: {cost}")
                if total_parts > 0:
                    print(f"Total parts automated: {parts_automated} out of {total_parts}, Adoption rate: {parts_automated/total_parts*100:.2f}%")
                    print(f"Total errors encountered: {Error}, error rate: {Error/total_parts*100:.2f}%")
                else:
                    print("No parts processed, so adoption and error rates are not available.")
            elif project_started == 'q':
                print("Exiting the process.")
                Confirm = False
            else:
                print("Invalid input for project started.")
        elif file_received == 'q':
            print("Exiting the process.")
            Confirm = False
        else:
            print("Invalid input for file received.")
    customer_satisfaction= int (input("Press rate the system (1-10): "))
    total_cycle_time = end_timer_fn(total_cycle_time)
    print(f"Total cycle time: {total_cycle_time:.2f} seconds")
    return cost, customer_satisfaction, total_cycle_time, parts_automated, total_parts, Error, dissemination_total_time, final_report_total_time, evaluation_of_report_total_time



def show_report(cost, customer_satisfaction, total_cycle_time, parts_automated, total_parts, Error, dissemination_total_time, final_report_total_time, evaluation_of_report_total_time):
    if total_parts == 0:
        messagebox.showinfo("Automation System Report", "No data was processed. Please run the process and try again.")
        return
    
    Adoption_rate = parts_automated/total_parts*100 # Example adoption rate
    Total_cycle_in_minutes = total_cycle_time / 60
    if total_parts > 0:
        Average_cycle_time_in_minutes = (dissemination_total_time / 60 + final_report_total_time / 60 + evaluation_of_report_total_time / 60) / total_parts
    else:
        Average_cycle_time_in_minutes = 0
    # Format values to 2 decimal places
    Adoption_rate_fmt = f"{Adoption_rate:.2f}"
    Total_cycle_in_minutes_fmt = f"{Total_cycle_in_minutes:.2f}"
    Average_cycle_time_in_minutes_fmt = f"{Average_cycle_time_in_minutes:.2f}"
    max_time = max(dissemination_total_time, final_report_total_time, evaluation_of_report_total_time)
    labels = []
    if dissemination_total_time == max_time:
        labels.append("Dissemination")
    if final_report_total_time == max_time:
        labels.append("Final Report")
    if evaluation_of_report_total_time == max_time:
        labels.append("Evaluation of Report")
    if len(labels) == 1:
        Delayed_step = labels[0]
    else:
        Delayed_step = " and ".join(labels)  # or "No specific bottleneck identified" if you prefer
    '''Delayed_step= max(dissemination_total_time, final_report_total_time, evaluation_of_report_total_time)
    if dissemination_total_time > final_report_total_time and dissemination_total_time > evaluation_of_report_total_time:
        Delayed_step = "Dissemination"
    elif final_report_total_time > dissemination_total_time and final_report_total_time > evaluation_of_report_total_time:
        Delayed_step = "Final Report"
    elif evaluation_of_report_total_time > dissemination_total_time and evaluation_of_report_total_time > final_report_total_time:
        Delayed_step = "Evaluation of Report"
    else:
        Delayed_step = "No specific bottleneck identified"'''
    Error_rate = Error / total_parts * 100 if total_parts > 0 else 0
    Error_rate_fmt = f"{Error_rate:.2f}"
    customer_satisfaction_rate= customer_satisfaction*10

    report = (
        "Automation System Report:\n\n"
        f"Total Cycle Time: {Total_cycle_in_minutes_fmt} minutes\n"
        f"Total Cost: ${cost}\n"
        f"Adoption Rate: {Adoption_rate_fmt} %\n"
        f"Error Rate: {Error_rate_fmt}%\n"
        f"Average Session Duration: {Average_cycle_time_in_minutes_fmt}\n"
        f"Most delayed step: {Delayed_step}\n"
        f"Customer Satisfaction: {customer_satisfaction_rate}%\n\n"
        "Overall, the system shows strengths"
    )
    
    print("DEBUG REPORT DATA:", report)  # Optional: for debugging
    messagebox.showinfo("Automation System Report", report)

if __name__ == "__main__":
    input("Press Enter to run the KPI system...")
    results = main()
    input("Press Enter to generate a report...")

    root = tk.Tk()
    root.title("Automation System Report Generator")
    root.geometry("300x100")
    cost, customer_satisfaction, total_cycle_time, parts_automated, total_parts, Error, dissemination_total_time, final_report_total_time, evaluation_of_report_total_time = results


    # Create a button to show the report
    report_button = tk.Button(
        root,
        text="Show Report",
        command=lambda: show_report(cost, customer_satisfaction, total_cycle_time, parts_automated, total_parts, Error, dissemination_total_time, final_report_total_time, evaluation_of_report_total_time)
    )
    report_button.pack(pady=50)

    # Run the application
    root.mainloop()

            
'''def report_generator (work_cycle_time, total_cycle_time, cost, parts_automated, total_parts, Error):
    print("Generating report...")
    Adoption_rate = 85  # Example adoption rate

    print ("The automation system's performance has been evaluated using several key performance indicators (KPIs). The average cycle time stands at 3.5 minutes, while the total cycle time, including wait times, averages 5.2 minutes, indicating some delays in the workflow. The total cost of the system is approximately $150,000, reflecting significant investment.")
    print (f"User adoption is at {Adoption_rate} , showing a strong acceptance but with potential for improvement. The error rate is recorded at 2.5%, suggesting a generally reliable system, although there is room for enhancing quality control. Users spend an average of 8 minutes per session, indicating engagement but also potential inefficiencies.")
    print ("Notably, the bottleneck occurs in the Data Processing stage, accounting for about 30% of the total cycle time. Addressing this bottleneck could significantly improve efficiency. Customer satisfaction is rated at 82%, which is positive but highlights areas for further enhancement.")
    print ("In summary, while the automation system demonstrates strengths in cycle time and user acceptance, there are challenges in total cycle time, error rates, and bottlenecks that need to be addressed to optimize overall performance.")
'''

# input which process is being done (choose among: planning, conducting and reporting)

# e.g reporting is chosen -> choose which process is being handled, 
# give suggestion too (Dissemination, Final report, Evaluation of report)

# Once clicked e.g dissemination 
# -> start work cycle time -> stop when hit submit****
# -> calculate total cost of the process -> sum every process until *****
# -> 2 parts to "automate" but only 1 will be used -> predetermined paragraph for each automated value, else nth***
# -> only automate one, fill the other info manually -> adoption part = sum ^ paragraph -> if both, sum of the sentences
# -> change the input of one manually inputted data -> error rate = input info that is wrong
# -> 

# hit submit -> stop total cycle time AND work cycle time
# store time in a variable (4)
# click submit -> continue = false (0)

# else write a message "Please click start when you begin" -> for code 1

# identify variables in (4) -> find max -> takes the longest -> report

# else write a message "Please wait to receive the documents" -> for code 2
# customer satisfaction**** -> report

# as long as continue = true, continue (0)
# Ask if the file is received or not, if yes move forward (1)
# start total cycle time -> stop when hit submit***** (2)

# Ask if the file has been started or not, if yes move forward, (3)
